def do_algebra(operator, operand):
    stack = []
    for i in range(len(operand) - 1):
        for j in range(i + 1, len(operand)):
            temp = []
            for k in range(len(operator)):
                if operator[k] == '+':
                    temp.append(operand[i] + operand[j])
                elif operator[k] == '-':
                    temp.append(operand[i] - operand[j])
                elif operator[k] == '*':
                    temp.append(operand[i] * operand[j])
                elif operator[k] == '//':
                    temp.append(operand[i] // operand[j])
                elif operator[k] == '**':
                    temp.append(operand[i] ** operand[j])
            stack.append(temp)
    return stack[0][len(operator) - 1]