def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    exp = 1
    for i in range(oper_len):
        result += operand[i] * exp
        operator = operator.replace('*', '', 1)
        if '**' in operator:
            exp = exp * int(operator.split('**')[1])
            operator = operator.replace('**', '', 1)
        elif '+' in operator:
            result += operand[i]
            operator = operator.replace('+', '', 1)
        elif '-' in operator:
            result -= operand[i]
            operator = operator.replace('-', '', 1)
        elif '//' in operator:
            result //= operand[i]
            operator = operator.replace('//', '', 1)
    if operator:
        result += int(operator)
    return result