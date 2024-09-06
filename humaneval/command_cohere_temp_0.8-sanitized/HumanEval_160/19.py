def do_algebra(operator, operand):
    result = 0
    # Calculate result using binary expression tree
    for i in range(0, len(operand) - 1):
        for j in range(i + 1, len(operand)):
            result += operator[i] * operand[j] * algebra(operator, operand, i + 1, j)
    # Return the final result
    return result
def algebra(operator, operand, i, j):
    if i == j:
        return operand[i]
    else:
        return operator[i] * algebra(operator, operand, i + 1, j) + algebra(operator, operand, i, j + 1)