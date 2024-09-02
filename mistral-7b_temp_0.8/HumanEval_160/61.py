
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
    op = operator[:]
    op.append('')
    result = operand[0]
    for i in range(0, len(op)):
        if i % 2 == 0:
            result = eval(op[i] + '(' + str(operand[i + 1]) + ',' + op[i + 1] + '(' + str(operand[i + 2]) + ',' + op[i + 2] + str(operand[i + 3]) + '))')
        else:
            result = eval(op[i] + '(' + str(operand[i + 1]) + ',' + op[i + 1] + str(operand[i + 2]) + ')')
    return result
