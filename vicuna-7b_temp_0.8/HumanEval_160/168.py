
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
    if len(operator) == len(operand) - 1 and all(i >= 0 for i in operator):
        expr = [operator.pop(0)]
        for i, op in enumerate(operator):
            expr.append(op[0])
        expr.append(operand.pop(0))
        result = eval(expr)
        for i in reversed(range(len(expr)-1)):
            if op[0] == operator[i+1]:
                expr.pop()
        return result
    else:
        return None
