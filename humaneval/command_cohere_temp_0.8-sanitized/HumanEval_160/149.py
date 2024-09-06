def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    exp = 1
    for i in range(oper_len):
        result += operand[i] * exp
        operator = operator.replace('*', '', 1)
        if '**' in operator:
            exp = exp * int(operator.replace('**', '', 1))
            operator = operator.replace('**', '', 1)
        elif '+' in operator:
            result += int(operator.replace('+', '', 1))
        elif '-' in operator:
            result -= int(operator.replace('-', '', 1))
        elif '//' in operator:
            result //= int(operator.replace('//', '', 1))
        else:
            return "Invalid operator!"
    return result