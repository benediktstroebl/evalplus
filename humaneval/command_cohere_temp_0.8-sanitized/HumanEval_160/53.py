def do_algebra(operator, operand):
    result = 0
    # Calculate the length of the shorter list to subtract from the length of the longer list
    len_diff = min(len(operator), len(operand)) - 1
    for i in range(len_diff):
        result += operator[i] * operand[i]
    result += operand[-1]
    return result