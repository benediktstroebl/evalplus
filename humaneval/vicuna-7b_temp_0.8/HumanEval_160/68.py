
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
    operand = [int(op[0]) for op in operand]
    result = 0
    for i in range(len(operand)):
        if i == 0:
            op = operator[0]
        else:
            op = operator[i-1]
        if i < len(operator):
            op2 = operator[i]
        else:
            op2 = '0'
        result = eval_binary_expression(op, operand[i-1], op2) + result
    return result
