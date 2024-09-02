
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
    operator_list = operator[:-1]
    operand_list = operand[1:]
    expression = ''.join(str(item) for item in operator_list)
    for i in range(len(operand_list)-1):
        operand_expr = ''.join(str(item) for item in operand_list[:i+1])
        operator_expr = ''.join(str(item) for item in operator_list)
        operator_expr = operator_expr[:-1]
        expression = expression.replace(operand_expr, '*'.join([str(item) for item in operator_expr]))
    if operator_list[-1] == '*':
        expression = expression.replace('*'.join([str(item) for item in operator_list[-2:]]), '**'.join([str(item) for item in operand_list[i]]))
    return eval(expression)
