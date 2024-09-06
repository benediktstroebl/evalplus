
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

    # Check operator length and operand length
    if len(operator)!= len(operand) - 1:
        raise Exception('operator list length does not equal to operand list length - 1')

    # Check if operator is valid
    for op in operator:
        if op not in ['+', '-', '*', '//', '**']:
            raise Exception('operator list has invalid operator')

    # Check if operand is valid
    for num in operand:
        if num < 0 or not isinstance(num, int):
            raise Exception('operand list has invalid operand')

    # Build algebra expression using operator list and operand list
    expression = ''
    for i in range(len(operator)):
        expression += '(' + str(operand[i]) + operator[i] + str(operand[i+1]) + ')'

    # Evaluate the expression
    result = eval(expression)

    # Return evaluation result
    return result

