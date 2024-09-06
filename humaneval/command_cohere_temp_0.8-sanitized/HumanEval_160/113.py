def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    assert oper_len == len(operand) - 1, "Operator list length must be equal to operand list length - 1"
    assert oper_len > 0 and oper_len == len(set(operator)), "Operator list must have unique elements"
    assert all(isinstance(i, int) and i >= 0 for i in operand), "Operand list must only contain non-negative integers"

    for i in range(len(operand) - 1):
        result += operator[i] * operand[i+1]

    return result
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]