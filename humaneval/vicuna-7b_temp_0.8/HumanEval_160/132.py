
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
    operand_len = len(operand)
    if operand_len < 2:
        return None

    if operator.startswith(('+', '*', '-')):
        operator = operator[1:]

    expression = []
    for i in range(operand_len):
        if i == 0 or i == 1:
            expression.append(operator[0])
        else:
            expression.append(operator[0]) + str(operand[i])

    if operator[-1] == '*':
        expression[-1] = str(eval(expression[-1] + '**0'))
    elif operator[-1] == '/':
        expression[-1] = str(eval(expression[-1] - '**0'))

    result = eval(expression[1:-1])
    return result
