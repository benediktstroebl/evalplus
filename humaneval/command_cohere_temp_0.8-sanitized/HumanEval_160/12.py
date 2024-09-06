def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        result += operand[i]
        for j in range(i+1, len(operand)):
            result += operand[j] * operator[i]
            if operator[i] == '/':
                result //= operand[j]
            if operator[i] == '^':
                result **= operand[j]
        if operator[i] == '-':
            result -= operand[j]
    return result