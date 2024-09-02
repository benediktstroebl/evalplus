
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
    # Left operand
    left_operand = operand[0]

    # Loop through the operand list
    for i in range(1, len(operand)):

        # For multiplication and division
        if operator[i - 1] == '*' or operator[i - 1] == '//':
            # Multiply or divide the left operand
            left_operand = left_operand * operand[i]

        # For addition and subtraction
        elif operator[i - 1] == '+' or operator[i - 1] == '-':
            # Add or subtract the left operand
            left_operand = left_operand + operand[i]

        # For exponentiation
        elif operator[i - 1] == '**':
            # Raise the left operand to the power of the right operand
            left_operand = left_operand ** operand[i]

    return left_operand

