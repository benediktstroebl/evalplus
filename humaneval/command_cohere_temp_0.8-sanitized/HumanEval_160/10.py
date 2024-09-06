def do_algebra(operator, operand):
    result = 0
    # Use the same length for operator and operand for avoiding out of index error
    for i in range(len(operator)):
        result += operator[i] * operand[i]
    return result