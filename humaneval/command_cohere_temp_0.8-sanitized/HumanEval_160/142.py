def do_algebra(operator, operand):
    result = 0
    len_op = len(operator)
    len_op -= 1
    for i in range(len_op):
        result += operand[i]
        for j in range(i+1, len(operand)):
            result += operator[i] * operand[j]
    return result