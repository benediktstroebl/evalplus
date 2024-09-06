
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
    # # First method, use recursion
    # if len(operator) == 0:
    #     return operand.pop(0)
    # else:
    #     op = operator.pop(0)
    #     if op == '+':
    #         return do_algebra(operator, operand) + do_algebra(operator, operand)
    #     elif op == '-':
    #         return do_algebra(operator, operand) - do_algebra(operator, operand)
    #     elif op == '*':
    #         return do_algebra(operator, operand) * do_algebra(operator, operand)
    #     else:
    #         return do_algebra(operator, operand) // do_algebra(operator, operand)

    # Second method, without using recursion
    import operator as op
    from functools import reduce

    operator_list = {'+':op.add,
                     '-':op.sub,
                     '*':op.mul,
                     '//':op.floordiv,
                     '**':op.pow}

    return reduce(operator_list[operator.pop(0)], operand)
