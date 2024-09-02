
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
    if len(operand) < 2:
        raise ValueError("operand list should be at least two operands")

    if len(operator) != len(operand) - 1:
        raise ValueError("operator list length should be equal to operand list minus one")

    def do_algebra_helper(operator, operand, start=0):
        if len(operator) == 0:
            return operand[start]
        if start == len(operand) - 1:
            return operand[start]
        return operator[0](
            do_algebra_helper(operator[1:], operand, start + 1),
            do_algebra_helper(operator[1:], operand, start + 2),
        )

    return do_algebra_helper(operator, operand)

