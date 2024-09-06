def do_algebra(operator, operand):
    result = 0
    oper_idx = 0
    for num in operand:
        if oper_idx == len(operator):
            break
        op = operator[oper_idx]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '//':
            result //= num
        else:
            result **= num
        oper_idx += 1
    return result