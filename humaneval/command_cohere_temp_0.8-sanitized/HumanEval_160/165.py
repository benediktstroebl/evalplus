def do_algebra(operator, operand):
    result = 0
    for op, num in zip(operator, operand):
        if   op == '+': result += num
        elif op == '-': result -= num
        elif op == '*': result *= num
        elif op == '//': result //= num
        elif op == '**': result **= num
    return result
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]