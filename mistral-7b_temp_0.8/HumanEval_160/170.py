
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
    # Your code here
    """
    1. check for 3 loops if not enough elements
    2. for each i,
    check if i is number
        append to numbers
    check if i is operator
        put in operations
    """
    # check for 3 loops
    if len(operator) != len(operand) - 1:
        return

    # create variables
    numbers = []
    operators = []
    # loop through list
    for i in range(len(operator)):
        # check if i is a number
        if operator[i] in ['+', '-', '*', '/', '**']:
            operators.append(operator[i])
        else:
            numbers.append(operator[i])

    # return correct answer
    return eval(str(numbers[0]) + operators[0] + str(numbers[1]))

