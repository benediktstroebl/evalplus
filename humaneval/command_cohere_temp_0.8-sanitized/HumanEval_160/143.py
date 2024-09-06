def do_algebra(operator, operand):
    stack = []
    for i in operand:
        stack.append(i)
    result = stack.pop()
    for i in range(len(operator) - 1):
        operator_name = operator[i]
        next_operand = stack.pop()
        if operator_name == '*':
            result = result * next_operand
        elif operator_name == '+':
            result = result + next_operand
        elif operator_name == '-':
            result = result - next_operand
        elif operator_name == '//':
            result = result // next_operand
        else:
            result = result ** next_operand
    return result