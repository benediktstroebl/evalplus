def do_algebra(operator, operand):
    stack = []
    for i in range(len(operand) - 1):
        for j in range(len(operator)):
            if operator[j] == '+':
                stack.append(operand[i] + operand[i + 1])
            elif operator[j] == '-':
                stack.append(operand[i] - operand[i + 1])
            elif operator[j] == '*':
                stack.append(operand[i] * operand[i + 1])
            elif operator[j] == '//':
                stack.append(operand[i] // operand[i + 1])
            elif operator[j] == '**':
                stack.append(operand[i] ** operand[i + 1])
    return stack.pop()