
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
    # Check if the operand list is empty
    if len(operand) == 0:
        return 0

    # Check if operator list is empty
    if len(operator) == 0:
        return 0

    # Check if the number of operators in operator list is greater than the number of operands in operand list
    if len(operator) > len(operand):
        return 0

    # Check if the operator is a valid operator for the operand
    if operator[0] not in operator['+', '-'] and operator[0] not in operator['*']:
        return 0

    # Create the algebraic expression
    expression = ''
    for i in range(len(operator)):
        if operator[i] == '+':
            expression = expression + operand[i]
        elif operator[i] == '-':
            expression = expression + operand[i]
        elif operator[i] == '*':
            expression = expression + str(operator[i+1])
        elif operator[i] == '/':
            expression = expression + str(operator[i+1])
        elif operator[i] == '**':
            expression = expression + str(operator[i+1])
        else:
            break

    # Evaluate the expression
    result = eval(expression)
    return result
