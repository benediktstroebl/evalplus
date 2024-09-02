
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
    num_operators = len(operator)
    num_operands = len(operand)
    if num_operators != num_operands - 1:
        return None

    # for now, we'll only have one operator, so we can just use the first one
    operator = operator[0]

    if operator == '+':
        return sum(operand)
    elif operator == '-':
        return operand[0] - operand[1]
    elif operator == '*':
        return prod(operand)
    elif operator == '/':
        return div(operand)
    elif operator == '**':
        return exp(operand)

    return None
