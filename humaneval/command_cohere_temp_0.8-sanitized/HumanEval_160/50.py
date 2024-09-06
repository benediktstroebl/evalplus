def do_algebra(operator, operand):
    result = 0
    # Handle exponentiation explicitly since python doesn't support ** operator in loops.
    exponentiation = [operand[0]**num for num in operand[1:]]
    for i in range(len(operand)-1):
        num = operand[i]
        for operation in operator:
            if operation == '+':
                num = num + result
            elif operation == '-':
                num = num - result
            elif operation == '*':
                num = num * result
            elif operation == '//':
                num = num // result
        result = num
    return result + exponentiation