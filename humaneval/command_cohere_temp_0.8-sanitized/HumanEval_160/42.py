def do_algebra(operator, operand):
    """
    Evaluates an algebraic expression built from given operators and operands.

    Args:
        operator (list): List of strings representing algebraic operations, such as '+', '-', '*', '**', '//'.
        operand (list): List of integers to be used in the expression.

    Returns:
        int: The result of the algebraic expression built from the provided operator and operand.

    Example:
        >>> do_algebra(['+', '*', '-'], [2, 3, 4, 5])
        9
    """
    if not operator or not operand:
        return None

    # Using recursion to build the expression from the bottom up
    def build_expression(op, operand):
        if len(operand) == 1:
            return operand[0]
        else:
            expression = build_expression(op[1], operand[1:])
            for i in range(len(op) - 1):
                expression = op[i] + expression
            return expression

    return build_expression(operator, operand)
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]