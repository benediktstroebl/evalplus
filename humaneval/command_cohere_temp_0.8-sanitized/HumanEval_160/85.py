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

    # Calculate the length of the operand list and make sure it's > 1
    operand_len = len(operand)
    if operand_len < 2:
        raise ValueError("Operand list must have at least two elements.")

    # Calculate the length of the operator list and make sure it's > 0
    operator_len = len(operator)
    if operator_len < 1:
        raise ValueError("Operator list must have at least one element.")

    # Check if the lengths of the two lists are as expected
    if operand_len - operator_len != 0:
        raise ValueError(f"Expecting lengths of operator and operand lists to differ by 1. Got {operand_len} and {operator_len} respectively.")

    # Initialize result to the first operand
    result = operand[0]

    # For each pair of elements in operator and operand, perform the operation
    for i in range(1, operand_len):
        result = operator[i - 1](result, operand[i])

    return result