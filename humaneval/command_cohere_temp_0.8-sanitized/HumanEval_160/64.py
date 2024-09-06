def do_algebra(operator, operand):
    result = 0
    # Calculate result using chained operations
    for i in range(len(operand) - 1):
        result = operand[i] * operator[i] / operand[i + 1]
    # Adding the last operand directly
    result += operand[-1]
    return result