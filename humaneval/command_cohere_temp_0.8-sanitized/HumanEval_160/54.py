def do_algebra(operator, operand):
    result = 0
    # Calculate result using the reversed expression
    for i in range(len(operand) - 1):
        result += operand[i] * globals()[operator[i]](operand[i + 1])
    return result