def do_algebra(operator, operand):
    stack = []
    for i in operand:
        stack.append(i)
    result = stack.pop()
    for i in range(len(operator)):
        operator = operator[i]
        if operator == '+':
            result += stack.pop()
        elif operator == '-':
            result -= stack.pop()
        elif operator == '*':
            result *= stack.pop()
        elif operator == '**':
            result **= stack.pop()
        elif operator == '/':
            numerator = stack.pop()
            denominator = stack.pop()
            result = numerator // denominator
        else:
            return "Error: Invalid operator"
    return result