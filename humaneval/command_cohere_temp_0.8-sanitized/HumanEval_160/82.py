def do_algebra(operator, operand):
    stack = []
    for i in range(len(operand) - 1):
        for j in range(i + 1, len(operand)):
            o1, o2 = operator[i], operator[j]
            num1, num2 = operand[i], operand[j]
            stack.append((o1, o2, num1, num2))
    stack.reverse()
    result = 0
    while stack:
        o1, o2, num1, num2 = stack.pop()
        if o1 == '+':
            result += num1
        elif o1 == '-':
            result -= num1
        elif o1 == '*':
            result *= num1
        elif o1 == '//':
            result //= num1
        elif o1 == '**':
            result **= num1
        else:
            return "Error: Invalid operator" 
    return result