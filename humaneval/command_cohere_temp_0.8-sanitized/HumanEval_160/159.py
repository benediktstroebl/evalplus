def do_algebra(operator, operand):
    stack = []
    for i in range(len(operand) - 1):
        for j in range(i + 1, len(operand)):
            item = operand[i]
            for k in range(j + 1, len(operand)):
                item = operator[k - j - 1](item, operand[k])
            stack.append(item)
    return stack[0]