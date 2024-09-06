def do_algebra(operator, operand):
    stack = []
    for i in range(len(operand) - 1):
        stack.append(operand[i])
    stack.append(operand[-1])
    result = stack[0]
    for i in range(1, len(stack)):
        operator_i = operator[i - 1]
        if operator_i == '+':
            result = result + stack[i]
        elif operator_i == '-':
            result = result - stack[i]
        elif operator_i == '*':
            result = result * stack[i]
        elif operator_i == '**':
            result = result ** stack[i]
        elif operator_i == '/':
            result = result // stack[i]
    return result