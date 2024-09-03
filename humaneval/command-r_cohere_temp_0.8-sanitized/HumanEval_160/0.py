def do_algebra(operator, operand):
    """
    Evaluates the algebraic expression built using the operator and operand lists.
    """
    assert len(operator) == len(operand) - 1
    assert all(isinstance(num, int) and num >= 0 for num in operand)
    assert len(operator) >= 1 and len(operand) >= 2

    result = operand[0]
    for op, num in zip(operator, operand[1:]):
        result = {"+": lambda x: result + x,
                 "-": lambda x: result - x,
                 "*": lambda x: result * x,
                 "//": lambda x: result // x,
                 "**": lambda x: result ** x}[op](num)
    return result