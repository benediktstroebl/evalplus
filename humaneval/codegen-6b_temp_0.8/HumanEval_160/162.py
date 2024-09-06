
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
    from operator import add, sub, mul, floordiv, pow
    
    def _do_op(nd_1, nd_2, op):
        if op == '+':
            return nd_1 + nd_2
        elif op == '-':
            return nd_1 - nd_2
        elif op == '*':
            return nd_1 * nd_2
        elif op == '/':
            return nd_1 // nd_2
        elif op == '**':
            return nd_1 ** nd_2
        raise Exception('Oops, invalid operator: {}'.format(op))

    # make sure len(operator) == len(operand) - 1
    if len(operator) != len(operand) - 1:
        raise Exception('Oops, len of operator({}) is different to that of operand({}) - 1'.
                        format(len(operator), len(operand)))

    # make sure operator has non-repeated elements
    if len(set(operator)) < len(operator) or len(set(operand)) < len(operand):
        raise Exception('Oops, operator, or operand do not have non-repeated elements')

    # make sure operator only contains '+', '-', '*', '/', '**'
    if operator.count('+') + operator.count('-') + operator.count('*') + operator.count('/') + operator.count('**') \
    not in (0, len(operator)):
        raise Exception('Oops, operator only contains '
                        '\'+\', \'-\', \'*\', and \'**\'')

    # make sure operand only contains non-negative integers
    for i in range(len(operand)):
        if operand[i] < 0:
            raise Exception('Oops, there is a negative in the operand')

    ops_map = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': floordiv,
        '**': pow,
    }
    return _do_op(operand[0], operand[1], operator