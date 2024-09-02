
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
    op_count = len(operator)
    operand_count = len(operand)

    if not 1 <= op_count <= operand_count - 1:
        raise ValueError("Operator list has the wrong length")

    if not all(x >= 0 for x in operand):
        raise ValueError("Operand list has negative integers")

    if not 1 <= len(operator[0]):
        raise ValueError("Operator list has the wrong length")

    if not operator[0][0] == operator[-1][0]:
        raise ValueError("Operator list is not closed")

    # Create the expression
    expression = operator[0]
    for i in range(1, op_count):
        expression = expression * operator[i]

    # Evaluate the expression
    result = 0
    for operand_i in range(operand_count):
        operand_i_val = operand[operand_i]
        if operand_i_val >= 0:
            result += operand_i_val * expression[operand_i]

    return result