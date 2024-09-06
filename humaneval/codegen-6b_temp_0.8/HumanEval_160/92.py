
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
    if len(operator) < 2 or len(operand) < 2:
        return None

    # make arrays to store the result
    len_operand = len(operand)
    result = [None for _ in range(len_operand)]

    # calculate each element
    for index in range(len_operand):
        result[index] = operator[index](operand[index], operand[index + 1]) if index + 1 < len_operand else operator[index](operand[index])

    return result
