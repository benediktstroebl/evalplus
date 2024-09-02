
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    # Add your code here
    def parse(operand, operator):
        # split the operand into 2 lists, using the operator index
        left_operand = operand[:operator]
        right_operand = operand[operator+1:]

        # convert the list into an integer
        left_operand = int("".join([str(i) for i in left_operand]))
        right_operand = int("".join([str(i) for i in right_operand]))
        
        # get the operation to perform
        operation = operator[operator]
        
        if operation == "+":
            return left_operand + right_operand
        elif operation == "-":
            return left_operand - right_operand
        elif operation == "*":
            return left_operand * right_operand
        elif operation == "//":
            return left_operand // right_operand
        elif operation == "**":
            return left_operand ** right_operand
    
    # loop through the operator list
    for i in range(len(operator)):
        operand = parse(operand, i)
        
    # return the result
    return operand
