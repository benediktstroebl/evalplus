def do_algebra(operator, operand):
    result = 0
    # Calculate result using the provided operations and operands
    for i in range(len(operand) - 1):
        result += operand[i] + operator.index(operator[i]) * operand[i + 1]
    result += operand[-1]

    # Remove the last operand since it was added twice
    return result - operand[-1]