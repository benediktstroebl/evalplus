
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
    # Check that the operator list is not empty
    if len(operator) == 0:
        return 0

    # Check that the operand list is not empty
    if len(operand) == 0:
        return 0

    # Check that the operator list has at least one operator
    if len(operator) == 1 and not isinstance(operator[0], tuple):
        return operator[0]

    # Check that the operator is not "//"
    if operator[0] == '/':
        return 0

    # Check that the operand list has at least two operands
    if len(operand) == 1:
        return 0

    # Get the operator and operand
    operator_index = operator.index(operator[0])
    operand_index = operand.index(operand[0])

    # Get the operands
    operands = operator[operator_index + 1: operator_index + operand[1] + 1]

    # Get the evaluation of the expression
    value = operands[operand_index]

    # Recursively evaluate any nested operands
    for i in range(1, len(operand)):
        value *= operands[i]

    return value
