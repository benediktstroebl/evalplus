
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
    # get operator string
    op = ' '.join(operator)
    # get operand
    val = operand[0]
    # get operator
    operator = operator[1:]
    # get number of operands
    num_ops = len(operator)
    # check if operator is valid
    if len(operator) < 1:
        raise ValueError("Operator list is empty")
    # check if operand is valid
    if len(val) != num_ops:
        raise ValueError("Number of operands in the operand list does not match the number of operators in the operator list")
    # get the result
    result = eval(op)
    return result