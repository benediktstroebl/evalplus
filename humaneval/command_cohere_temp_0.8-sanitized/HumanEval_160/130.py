def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    assert oper_len == len(operand) - 1, "Operator list length must be equal to operand length - 1"
    for i in range(oper_len):
        result += operand[i] * operator[i]
    return result