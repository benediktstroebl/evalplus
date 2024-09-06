def do_algebra(operator, operand):
    # Type checking and length checking
    assert all(isinstance(i, (int, str)) for i in operand)
    assert all(isinstance(i, (str)) for i in operator)
    assert len(operator) == len(operand) - 1

    # Mapping dictionary to hold corresponding operands
    mapping = {i: operand for i in range(len(operand))}

    # Building and evaluating the expression
    result = eval(f"{{}}".format(*operator, **mapping))

    return result