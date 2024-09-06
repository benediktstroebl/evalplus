def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        result += operand[i]
        for j in range(i+1, oper_len):
            result += operator[i] * operand[j]
    return result