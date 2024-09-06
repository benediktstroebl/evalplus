def do_algebra(operator, operand):
    result = 0
    stack = [operand[0]]
    for i in range(1, len(operand)):
        item = stack.pop()
        op = operator[i - 1]
        if op == '+':
            result += item
        elif op == '-':
            result += item
        elif op == '*':
            result += item * stack.pop()
        elif op == '//':
            result += item // stack.pop()
        elif op == '**':
            result += item ** stack.pop()
        stack.append(result)
    return result