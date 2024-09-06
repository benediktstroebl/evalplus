def do_algebra(operator, operand):
    result = 0
    # Calculate result using chained operations
    for i in range(len(operand) - 1):
        result = operand[i] + operator[i] * result
        if i != len(operand) - 2:
            result = result + operand[i + 1]
    return result