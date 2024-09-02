
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
    assert len(operator) == len(operand) - 1
    assert all(isinstance(x, int) and x >= 0 for x in operand)
    assert all(x in ['+', '-', '*', '//', '**'] for x in operator)
    import operator as op
    op_map = {'+': op.add, '-': op.sub, '*': op.mul, '//': op.floordiv, '**': op.pow}
    result = operand[0]
    for i, op in enumerate(operator):
        result = op_map[op](result, operand[i + 1])
    return result
