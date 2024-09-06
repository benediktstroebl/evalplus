def do_algebra(operator, operand):
    result = 0
    # Use the same length for loops for better performance
    o_len = len(operator)
    assert o_len == len(operand) - 1, "Operator list length must be the Operand list length minus one."
    for i in range(o_len):
        result += operand[i] * operator[i]
    return result