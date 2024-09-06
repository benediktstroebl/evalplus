def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        num = operand[i]
        for j in range(i + 1, len(operand)):
            num = operator[i] + '(' + str(num) + ',' + str(operand[j]) + ')' + operator[j + 1]
            if operator[i] == '**':
                num = num.replace('**', '^')
            result += eval(num)
    return result