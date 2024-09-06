def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    expect = len(operand) - 1
    half_expect = expect // 2
    curr_expect = 0

    for i in range(len(operand) - 1):
        if operator[i % oper_len] == '+':
            result += operand[i]
        elif operator[i % oper_len] == '-':
            result -= operand[i]
        elif operator[i % oper_len] == '*':
            result *= operand[i]
        elif operator[i % oper_len] == '//':
            result //= operand[i]
        elif operator[i % oper_len] == '**':
            result **= operand[i]
        curr_expect += 1
        if curr_expect == half_expect:
            result *= operand[i + 1]
            curr_expect = 0

    if expect % 2 == 0:
        result *= operand[-1]
    return result