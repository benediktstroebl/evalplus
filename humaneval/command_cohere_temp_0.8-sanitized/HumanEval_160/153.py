def do_algebra(operator, operand):
    """
    Build and evaluate an algebraic expression using two input lists.

    Args:
        operator (list): List of algebra operations, such as ['+', '*', '-'].
        operand (list): List of integers to be used in the expression, e.g.[2, 3, 4, 5].

    Returns:
        int: Result of the algebraic expression created from the two input lists.

    Example:
        >>> do_algebra(['+', '*', '-'], [2, 3, 4, 5])
        9
    """
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator list length must be equal to operand list length minus one.")
    expression = ""
    for i in range(len(operand) - 1):
        expression += operator[i]
        expression += "("
        expression += str(operand[i])
        expression += ", "
        expression += str(operand[i + 1])
        expression += ")"
    expression += operator[-1]
    expression += "("
    expression += str(operand[-1])
    expression += ")"
    return eval(expression)