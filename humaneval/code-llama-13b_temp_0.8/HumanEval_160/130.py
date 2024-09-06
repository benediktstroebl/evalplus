
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
    if len(operator) + 1 != len(operand):
        raise ValueError("The length of operator list is equal to the length of operand list minus one")

    if len(operator) == 0:
        raise ValueError("Operator list has at least one operator")

    if len(operand) < 2:
        raise ValueError("Operand list has at least two operands")

    for i in operand:
        if i < 0:
            raise ValueError("Operand is a list of of non-negative integers")

    op_list = list(zip(operator, operand[1:]))

    # Add all the operands
    result = operand[0]

    # Perform the operations in the operator list
    for (o, a) in op_list:
        if o == "+":
            result += a
        elif o == "-":
            result -= a
        elif o == "*":
            result *= a
        elif o == "//":
            result //= a
        elif o == "**":
            result **= a
        else:
            raise ValueError("Unknown operator")

    return result
