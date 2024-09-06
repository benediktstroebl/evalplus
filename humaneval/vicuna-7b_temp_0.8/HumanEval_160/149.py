
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
    operands = operand[1:]
    expression = []
    for i in range(len(operator) - 1, -1, -1):
        expression.append(operator[i])
        expression.append(operand[0])
        operand = operands.copy()
        operand[0] = 0
        while operand[0] < 0:
            operator = operator[:-1]
            operand = operands.copy()
            operand[0] = 0
    expression.append(operator[i])
    expression.append(operand[0])
    result = 0
    for i in range(len(expression)):
        if expression[i] == '*':
            result = result * expression[i+1]
        elif expression[i] == '/':
            result = result / expression[i+1]
        elif expression[i] == '**':
            result = result ** expression[i+1]
    return result
