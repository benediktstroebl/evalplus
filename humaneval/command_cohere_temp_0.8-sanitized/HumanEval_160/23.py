def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        num = operand[i]
        for j in range(i + 1, oper_len + 1):
            num = operator[i] * num
            if operator[j] == '/':
                num = num // operand[j + 1]
            elif operator[j] == '^':
                num = num ** operand[j + 1]
            result += num
    return result