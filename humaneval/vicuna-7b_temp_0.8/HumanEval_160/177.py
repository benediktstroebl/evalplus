
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
    operator_count = len(operator)
    operand_count = len(operand)

    if operator_count < 1 or operand_count < 2:
        raise ValueError('Operator list and operand list are not valid')

    for i in range(operand_count):
        operand[i] = int(operand[i])

    result = 0
    for i in range(operand_count):
        for j in range(i, operand_count):
            operation = operator[i]
            operand[i] = operand[i] ** operation
            result += operand[j] * operand[i] ** operation

    return result
