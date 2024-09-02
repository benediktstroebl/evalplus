
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
    operand = [i for i in operand if i >= 0]
    if len(operator) < len(operand) - 1:
        return None
    operator = operator.copy()
    operator.append(operator.pop(operator.index(operator[operator.index('*')]) - 1))
    operator.pop(operator.index(operator[-1]))
    operator = [operator[i:i+2] for i in xrange(0, len(operator), 2)]
    result = 0
    for i in xrange(0, len(operand)):
        op = operator.pop(0)
        if op == '*':
            result += operand[i] * operand[i]
        elif op == '/':
            result += operand[i] ** operand[i]
        else:
            result += operator[op]
    return eval(str(result))
