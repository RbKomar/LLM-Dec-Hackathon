modifyPrompt = """
    Your task is to modify the function provided below. Initially, list all the variables and define what they represent. Then analyze the processes and calculations that have been performed in this function. Next, define which of the listed variables relates to the problem described in the query. Based on the acquired knowledge and context, make the required modification to implement the modification requested in the query. Then, proceed sequentially higher in the function hierarchy and verify whether these changes will cause errors in higher-level functions. If not, conclude the process and return only the modified function. Remember, return only whole modified function, do not cut it and information is is Destroying.

    EXAMPLE:

    Q: 
    Question: Modify the function to calculate a student's average grade so that the final exam counts as 40percent of the overall grade, regardless of the number of grades.

    Context: 
    main function: 
    def calculate_average(grades):
        if not grades:
            return 0
        return sum(grades) / len(grades)

    Function relations:[ idx:0,name: calculate_average,idx:1,name: generate_student_report,]

    Code of other functions: 
    def generate_student_report(student_id, grades):
        average = calculate_average(grades)
        return average

    Process of thinking:

    Variables in the Original Function:
    
    grades: A list of numerical values representing the student's grades.
    Average: Is the return of calculate_average(grades) function

    Process and Calculations:
    The function calculates the average by summing all grades and dividing by the number of grades.

    Identifying Relevant Variables:
    The grades list is relevant, especially the last element, which we assume is the final exam.

    Required Modification:
    Modify the function to calculate the average where the final exam (last element in grades) counts as 40% of the overall grade

    Check parent functions after modification: 
    Changes will not cause errors inside higher functions. End of process, return the modified function  and answear if it destroys higher function.

    A:

    Function:  

    def calculate_average(grades):
        if not grades:
            return 0
        final_exam_weight = 0.4  # 40% weight for the final exam
        other_grades_weight = 0.6  # Weight for other grades

        final_exam = grades[-1]
        other_grades = grades[:-1]

        # Calculate the average of other grades
        if other_grades:
            other_average = sum(other_grades) / len(other_grades)
        else:
            other_average = 0

        # Calculate the new weighted average
        weighted_average = (other_grades_weight * other_average) + (final_exam_weight * final_exam)
        return weighted_average

    End of Function  

    Is Destroying: false
    

     Q:
     Question: {question}
     Context: {context}   
    """


analyzePrompt = """
    Choose based on your knowledge one, the most appropriate function/class or module considering given question.Analyze the following Python choosen one in detail. Describe its, list and explain each variable and its role, examine the processes and calculations performed, identify any key logic or algorithms used, and explain the expected output. Based on your analysis, determine if there are any areas for optimization or potential errors. Conclude by summarizing  overall functionality and its potential applications.
    Remember to do this step by step.

    Q: 
    Question: Please provide me analysis of how is discounted price is calculated.
    Context: 
    def calculate_discounted_price(price, discount_rate):
    if discount_rate < 0 or discount_rate > 1:
        raise ValueError("Invalid discount rate. Please provide a rate between 0 and 1.")
    
    discount = price * discount_rate
    discounted_price = price - discount
    return discounted_price
    


    A:
    Name of the Function oraz Class or module: calculate_discounted_price
    Purpose of the Function:

    The function calculate_discounted_price calculates the discounted price of an item based on its original price and a discount rate.
    Variables:

    price: Represents the original price of the item. It is a numeric value.
    discount_rate: Represents the rate of the discount. It is a numeric value expected to be between 0 (no discount) and 1 (100% discount).
    discount: A calculated variable representing the amount of discount in currency. It is derived by multiplying price by discount_rate.
    discounted_price: The final price after applying the discount. It is calculated by subtracting discount from price.
    Processes and Calculations:

    The function first checks if the discount_rate is valid (i.e., between 0 and 1). If not, it raises a ValueError.
    Then, it calculates the discount amount by multiplying the price by the discount_rate.
    It calculates the discounted_price by subtracting the discount from the price.
    Finally, it returns the discounted_price.
    Key Logic:

    Input validation: Ensures the discount_rate is within a reasonable range.
    Discount calculation: Applies a straightforward arithmetic operation to determine the discount and the final price.
    Expected Output:

    The function returns the discounted_price, which is the price of the item after applying the discount.
    Optimization and Potential Errors:

    The function correctly handles invalid discount rates by raising an error.
    It could be optimized by adding checks for negative prices or extremely high discount rates that might indicate input errors.
    Overall Functionality and Applications:

    This function is useful in e-commerce systems, retail software, or anywhere item prices need to be adjusted based on discounts.
    Its clear input validation and straightforward logic make it reliable for financial calculations involving discounts.


Q:
Question: {question}
Context: {context}
    """

addPrompt = """
Your task is to design and develop a new function from the ground up. Begin by clearly defining the purpose and objectives of the function based on the requirements outlined in the query. Next, determine the inputs and outputs of the function: identify what data the function will receive and what it should return. As you outline the logic and algorithm that the function will implement to achieve its goals, consider any necessary calculations, data processing steps, or decision-making processes that need to be included.
Furthermore, examine the context in which this function will be used, especially in relation to other existing functions. Ensure that your new function is compatible with these functions, both in terms of data types and the flow of information. If the new function needs to interact with or complement existing functions, carefully design its interface and internal workings to integrate smoothly within the existing codebase. 
Once the core functionality and compatibility considerations are outlined, write the complete function code, ensuring it adheres to best practices for readability, efficiency, and seamless integration with the existing functions.  Return only created function.

    EXAMPLE:

    Q: 
    Question: Develop a new function that calculates the average of the sum and product of two numbers.

    Context: 
    def add_numbers(a, b):
        //Add to values
        return a + b

    def multiply_numbers(a, b):
        //multiply two numbers
        return a * b

    Process of thinking:
    Steps to Create the New Function
    Define the Purpose:

    The new function's purpose is to calculate the average of the sum and product of two numbers.
    Determine Inputs and Outputs:

    Inputs: Two numerical values (let's call them x and y).
    Output: A single numerical value representing the average.
    Outline the Logic:

    The function will use the existing add_numbers and multiply_numbers functions.
    It will first calculate the sum of x and y using add_numbers.
    Then, it will calculate the product of x and y using multiply_numbers.
    Finally, it will calculate the average of these two values.
    Write the Function Code

    A:
        Generated function:
        def average_sum_product(x, y):
            //Calculate the average of the sum and product of two numbers.
            sum_of_numbers = add_numbers(x, y)
            product_of_numbers = multiply_numbers(x, y)
            average = (sum_of_numbers + product_of_numbers) / 2
            return average
        End of generated function

     Q:
     Question: {question}
     Context: {context}   
    """
