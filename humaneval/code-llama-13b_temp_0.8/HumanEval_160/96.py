
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

    # Set the first operand.
    result = operand.pop(0)

    # If the operator list is not empty.
    while operand:
        op = operand.pop(0)

        # Perform the calculation.
        if op == '+':
            result += operand.pop(0)

        elif op == '-':
            result -= operand.pop(0)

        elif op == '*':
            result *= operand.pop(0)

        elif op == '//':
            result //= operand.pop(0)

        elif op == '**':
            result **= operand.pop(0)

    return result
