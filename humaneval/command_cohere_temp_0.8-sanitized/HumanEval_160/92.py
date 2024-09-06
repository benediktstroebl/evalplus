def do_algebra(operator, operand):
    result = 0
    # Use the same length for operant and operand for stopping the loop
    for i in range(len(operand)):
        for oper in operator:
            result += oper == '+'  and operand[i] or 0
            result -= oper == '-'  and operand[i] or 0
            result *= oper == '*'  and operand[i] or 1
            result //= oper == '//'  and operand[i] or 1
            result **= oper == '**'  and operand[i] or 1
    return result