def do_algebra(operator, operand):
    result = 0
    oper_idx = 0
    for num in operand:
        result += operator[oper_idx] * num
        oper_idx += 1
    return result