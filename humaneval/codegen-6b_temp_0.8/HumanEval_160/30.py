
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
    operand_len = len(operand)
    operator_len = len(operator)

    if operand_len == 1:
        return operand[0]

    if operand_len == 2:
        return operator[0](operand[0], operand[1])

    for op in operator:
        if operator.index(op) == 0:
            result = operator[0](operand[0], operand[1])
        elif operator.index(op) == operator_len - 1:
            result = operator[operator_len - 1](result, operand[operator_len])
        else:
            result = operator[op](result, operand[operator.index(op) + 1])

    return result
