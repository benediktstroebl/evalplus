
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
    if len(operator) < 1:
        raise ValueError('Operator list is too short')
    if len(operand) < 2:
        raise ValueError('Operand list is too short')
    operator_length = len(operator)
    operand_length = len(operand)
    if operator_length != operand_length - 1:
        raise ValueError('Operator list and operand list have different lengths')
    operand_value = operand[0]
    for operator_item in operator:
        operand_value = eval(operator_item + operand_value)
    return operand_value