def do_algebra(operator, operand):
    """
    Evaluate an algebraic expression built from two lists using basic operations.

    :param operator: List of basic algebra operations like '+', '-', '*','//', '**'.
    :param operand: List of integers used as operands.
    :return: Evaluated expression as an integer.
    """
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator list should be of length one less than the operand list.")

    expression = ""
    i = 0
    while i < len(operand) - 1:
        expression += operator[i]
        expression += "("
        expression += str(operand[i])
        i += 1
        if i < len(operand) - 1:
            expression += ", "
        else:
            expression += ")"

    expression += operator[i]
    expression += "("
    expression += str(operand[i])
    expression += ")"

    return eval(expression)
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]