def do_algebra(operator, operand):
    result = 0
    # Calculate result using predefined expressions
    for i in range(len(operand) - 1):
        expression = operand[i]
        for j in range(i + 1, len(operand)):
            expression = expression * operator[j - i - 1] + operand[j + 1]
        result += expression
    return result