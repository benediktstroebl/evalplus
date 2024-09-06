
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
    # Get the length of operands
    length_operands = len(operand)

    # Get the length of operators
    length_operators = len(operator)

    # Initialize result to the first operand
    result = operand[0]

    # If there is a second operand, add it to the result
    if length_operands > 1:
        # Get the operator between the first and second operands
        operator_between_first_and_second_operands = operator[0]

        # If there is an operator between the first and second operands, apply it to the operands
        if operator_between_first_and_second_operands:
            result = operator[0](operand[0], operand[1])

    # Iterate through the remaining operators and operands
    for i in range(length_operators - 1):
        # Get the operator between the current operand and the next operand
        operator_between_current_and_next_operands = operator[i + 1]

        # If there is an operator between the current operand and the next operand, apply
