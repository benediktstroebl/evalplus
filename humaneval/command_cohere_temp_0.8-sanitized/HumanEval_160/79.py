def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        result += operand[i] * eval(f'{operator[i]}{{i+1}}')
    return result