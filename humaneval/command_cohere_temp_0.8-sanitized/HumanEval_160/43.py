def do_algebra(operator, operand):
    stack = []
    for i in operand:
        stack.append(i)
    for j in range(1, len(operator)):
        top1 = stack.pop()
        top2 = stack.pop()
        stack.append(operator[j] + top1 + ' ' + top2 + '=' + str(eval(top1 + ' ' + top2)))
    return stack.pop()