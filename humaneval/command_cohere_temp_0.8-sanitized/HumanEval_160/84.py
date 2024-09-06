def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        num = operand[i]
        for j in range(i+1, oper_len):
            num = operator[i] * num + operand[j]
        result += num
    return result