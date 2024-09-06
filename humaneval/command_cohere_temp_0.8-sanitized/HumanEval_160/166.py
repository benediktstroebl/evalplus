def do_algebra(operator, operand):
    result = 0
    oper_idx, operand = len(operator) - 1, len(operand) - 1
    for i in range(len(operator)):
        result += operand[i] * operator[i]
        if oper_idx > i:
            result += operand[oper_idx] * operand[i]
        elif oper_idx < i:
            result += operand[i] * operand[oper_idx]
        oper_idx -= 1
    return result