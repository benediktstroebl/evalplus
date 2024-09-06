def do_algebra(operator, operand):
    result = 0
    # Remove trailing underscore to avoid deprecation warning in Python 3.8+
    for i in range(len(operand)-1):
        result += operator[i] * operand[i+1]
    return result