def do_algebra(operator, operand):
    result = 0
    # Calculate result using a loop to enforce the constraint of a minimal operator list and a minimal operand list
    for i in range(len(operand) - 1):
        result += operator[i] * operand[i+1]
    return result