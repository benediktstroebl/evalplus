
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
    operands = [operand[0]]
    operator_map = {}
    for i in range(len(operand)-1):
        operator_map[operator[i]] = operand[i+1]
    expr = []
    for j in operator:
        if j in operator_map:
            expr.append(operator_map[j]*operand[j])
        else:
            expr.append(operator[j])
    if operator[-1] in operator_map:
        result = operator_map[operator[-1]]
    else:
        result = eval(operator[-1])
    result = eval(result)
    result = result[0]
    return result
