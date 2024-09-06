def do_algebra(operator, operand):
    result = 0
    # Calculate result using brute force, iterating through all combinations of operands and operators.
    for i in range(len(operand)):
        for j in range(i + 1, len(operand)):
            for oper in operator:
                result += operand[i] * eval(f'{oper}({operand[j]})')
    return result