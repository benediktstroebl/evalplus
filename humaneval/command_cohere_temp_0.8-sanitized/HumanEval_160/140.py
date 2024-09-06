def do_algebra(operator, operand):
    result = 0
    # Handle exponentiation separately, as it needs to be iterated through both lists
    exponentiation_result = [operand[0] ** operand[1]] if '**' in operator else []

    for op in operator:
        if   op == '+': result += operand[0]
        elif op == '-': result -= operand[0]
        elif op == '*': result *= operand[0]
        elif op == '//': result //= operand[0]
        elif op == '**': exponentiation_result.append(operand[0] ** operand[1])
        operand = [operand[1]] if op == '**' else operand[1:]

    return result + exponentiation_result[0] if exponentiation_result else result