def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    expect = len(operand) - 1
    for i in range(expect):
        result += operand[i]
        for j in range(oper_len):
            if operator[j] == '+':
                result += operand[i + 1]
            elif operator[j] == '-':
                result -= operand[i + 1]
            elif operator[j] == '*':
                result *= operand[i + 1]
            elif operator[j] == '//':
                result //= operand[i + 1]
            elif operator[j] == '**':
                result **= operand[i + 1]
        i += 1
    return result