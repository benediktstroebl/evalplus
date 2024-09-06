
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
    op, oper = operator, operand
    while len(op) != 0:
        op.pop(0)
        i = op.pop(0)
        if i == '+':
            oper.pop(0)
            oper.pop(0)
            oper.insert(0, oper[0] + oper[1])
        elif i == '-':
            oper.pop(0)
            oper.pop(0)
            oper.insert(0, oper[0] - oper[1])
        elif i == '*':
            oper.pop(0)
            oper.pop(0)
            oper.insert(0, oper[0] * oper[1])
        elif i == '//':
            oper.pop(0)
            oper.pop(0)
            oper.insert(0, oper[0] // oper[1])
        elif i == '**':
            oper.pop(0)
            oper.pop(0)
            oper.insert(0, oper[0] ** oper[1])
    return oper[0]

