def do_algebra(operator, operand):
    result = 0
    # Calculate result using the recursive algorithm
    for i in range(len(operand) - 1):
        result += operand[i] * functools.reduce(operator[i], operand[i+1:])
    result += operand[-1]

    return result