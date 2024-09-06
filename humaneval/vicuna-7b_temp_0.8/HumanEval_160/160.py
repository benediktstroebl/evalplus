
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
    operands = operand[:-1]
    expression = ''
    for i, op in enumerate(operator):
        if i == 0:
            expression = expression + str(operands[0])
        else:
            expression = expression + operator[i-1] + str(operands[0])
    expression = expression[:-1]
    if operator[len(operator)-1] == '*':
        result = eval(expression)
        result = result ** int(operator[len(operator)-2])
        return result
    elif operator[len(operator)-1] == '/':
        result = eval(expression)
        result = result // int(operator[len(operator)-2])
        return result
    else:
        return eval(expression)
