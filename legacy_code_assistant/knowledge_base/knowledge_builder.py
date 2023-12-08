import ast
from typing import List, Tuple

from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings


# TODO: i tu tez zamontuj tego faissa
class KnowledgeBaseBuilder:
    """
    A class used to represent a Knowledge Base Builder.

    Attributes
    ----------
    processor : EmbeddingProcessor
        an instance of the EmbeddingProcessor class
    index_name : str
        the name of the index used in Faiss
    index : FaissStore
        the FaissStore instance
    """

    def __init__(self, index_name='code-search', model_name='microsoft/codebert-base'):
        """Initialize the Embedding Processor and FaissStore."""
        self.index_name = index_name

        self.model_name = model_name
        self.processor = HuggingFaceEmbeddings(model_name=self.model_name)
        self.vectorstore = None

    def upload_to_faiss(self, data):
        """Encode the data and upload it to Faiss."""

        strings = list(data.values())
        if self.vectorstore is None:
            self.vectorstore = FAISS.from_texts(
                texts=strings, 
                embedding=self.processor,
            )
        else:
            self.vectorstore.add_texts(
                texts=strings, 
                embedding=self.processor,
            )

    def search(self, query: str, k: int = 1) -> List[Tuple[str, float]]:
        """From a query, find the elements corresponding based on personal information stored in vectordb.
        Euclidian distance is used to find the closest vectors.

        Args:
        query (str): Question asked by the user.
        vectordb_dir (str, optional): Path to the vectordb. Defaults to config.VECTORDB_DIR.

        Returns:
        List[Tuple[Document, float]]: Elements corresponding to the query based on semantic search, associated
        with their respective score.
        """

        results = self.vectorstore.similarity_search_with_score(query=query, k=k)
        return results

    def save_index(self):
        """Save the index."""
        self.vectorstore.save_local(self.index_name)

    def load_index(self):
        """Load the index."""
        self.vectorstore = FAISS.load_local(self.index_name, embeddings =self.processor)



class CodeAnalyzer:
    """
    A class used to analyze code files.

    Attributes
    ----------
    code_files : list
        a list of code files to analyze
    """

    def __init__(self, code_files):
        self.code_files = code_files

    @property
    def analyzed(self):
        """Return a list of analyzed functions."""
        return [self.extract_function_info(item) for file in self.code_files for item in
                ast.walk(ast.parse(open(file, 'r').read())) if isinstance(item, ast.FunctionDef)]

    @staticmethod
    def extract_function_info(function_node):
        """
        Extract function information.

        Returns
        -------
        dict
            a dictionary containing function name and function docstring.
        """
        return {'name': function_node.name, 'docstring': ast.get_docstring(function_node)}

if __name__ == '__main__':
    kbb = KnowledgeBaseBuilder()
    kbb.upload_to_faiss({'test': 'def test():\n    pass'})
    kbb.save_index()

    kbb2 = KnowledgeBaseBuilder()
    kbb2.load_index()

    print(kbb.search('def test():\n    pass'))
    print(kbb2.search('def test():\n    pass'))

    print(kbb.search('all'))
    print(kbb2.search('ok'))

