
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
    # Initialize the expression string
    expression = str(operand[0])

    # Convert the operator and operand lists to python lists
    operator = list(operator)
    operand = list(operand)

    # The number of operators
    N = len(operator)

    # Loop over the operator and operand
    for i in range(N):
        # Add the operator and operand in expression string
        expression += operator[i] + str(operand[i+1])

    # Evaluate the expression and return the result
    return eval(expression)

