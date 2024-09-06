def do_algebra(operator, operand):
    result = 0
    # Handle exponentiation explicitly
    exp_op = operator.index('**')
    if exp_op != -1:
        result += operand[exp_op] ** operand[exp_op - 1]
    else:
        result += operand[0]
    # Handle remaining operations using a loop
    for i in range(1, len(operand) - 1):
        result += operand[i] * operand[i + 1]
        op = operator[i]
        if op == '-':
            result -= operand[i + 2]
        elif op == '/':
            result //= operand[i + 2]
        else:
            result += operand[i + 2]
    return result