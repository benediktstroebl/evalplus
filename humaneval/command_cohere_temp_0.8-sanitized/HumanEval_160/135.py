def do_algebra(operator, operand):
    result = 0
    # Use loops to create and evaluate the expression
    for op, num in zip(operator, operand):
        if   op == '+': result += num
        elif op == '-': result -= num
        elif op == '*': result *= num
        elif op == '//': result //= num
        elif op == '**': result **= num
    return result