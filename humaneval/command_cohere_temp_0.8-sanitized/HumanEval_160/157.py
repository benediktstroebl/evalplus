def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    assert oper_len == len(operand) - 1, "Operator list length must be equal to the length of operand list minus one."
    assert oper_len > 0 and oper_len == len(set(operator)), "Operator list must have at least one unique element."

    # The following lines should be updated when implementing new operations
    operations = {
        '+': result.__iadd__,
        '-': result.__isub__,
        '*': result.__imul__,
        '//': result.__itruediv__,
        '**': result.__imod__
    }
    operands = list(operand)

    for i in range(oper_len):
        idx_1, idx_2 = i, i + 1
        term1 = operand[idx_1]
        term2 = operand[idx_2]
        oper = operator[i]
        if oper == '*':
            result *= term1 * term2
        elif oper == '**':
            result *= term1 ** term2
        elif oper == '+':
            result += term1 + term2
        elif oper == '-':
            result += term1 - term2
        else:
            result += term1 // term2
        result = operations[oper](result)
    return result