
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
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list is not equal to the length of operand list minus one")
    if not operator[0] in ['+', '-', '*', '/']:
        raise ValueError("Operator list must contain at least one operator")
    if not operand[0] in [0, 1]:
        raise ValueError("Operand list must contain at least two operands")
    
    operands = operand[1:]
    result = operator[0]
    for i in range(1, len(operand)):
        if operator[i] == '+':
            result = result + operands[i]
        elif operator[i] == '-':
            result = result - operands[i]
        elif operator[i] == '*':
            result = result * operands[i]
        elif operator[i] == '/':
            if operands[i] == 0:
                raise ValueError("Cannot divide by zero")
            result = result / operands[i]
        elif operator[i] == '**':
            if not operands[i] % 2 == 0:
                raise ValueError("Operand must be even")
            result = pow(result, operands[i])
    return result
