def do_algebra(operator, operand):
    result = 0
    # Handle exponentiation explicitly, as it needs to be iterated through differently
    if "**" in operator:
        for i in range(len(operand)):
            result += operand[i] ** operator.index("**")
        return result
    # Handle other operations through recursive multiplication
    for i in range(len(operand)):
        result += operand[i] * do_algebra(operator, operand[i:])
    return result