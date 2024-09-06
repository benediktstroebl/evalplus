def do_algebra(operator, operand):
    result = 0
    oper_len = len(operator)
    expect = len(operand) - 1

    # Validate the input lengths
    if oper_len != expect:
        raise ValueError(f"Operator length ({oper_len}) does not match expected length ({expect})")

    # Validate the min length of operand list
    if expect < 2:
        raise ValueError("Operand list must have at least two elements")

    # Loop through and solve the expression
    for i in range(expect):
        result += operand[i]
        for j in range(len(operator)):
            if j == i:
                continue
            if operator[j] == '+':
                result += operand[j + 1]
            elif operator[j] == '-':
                result -= operand[j + 1]
            elif operator[j] == '*':
                result *= operand[j + 1]
            elif operator[j] == '//':
                result //= operand[j + 1]
            elif operator[j] == '**':
                result **= operand[j + 1]
    return result