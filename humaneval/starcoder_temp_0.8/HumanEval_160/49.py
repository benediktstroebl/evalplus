
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
    op_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '//': operator.floordiv,
        '**': operator.pow
    }

    i = 0
    while i < len(operator):
        op = operator[i]
        op = op_map[op]
        i += 1
        operand[i - 1] = op(operand[i - 1], operand[i])
        operand.pop(i)
    return operand[0]
