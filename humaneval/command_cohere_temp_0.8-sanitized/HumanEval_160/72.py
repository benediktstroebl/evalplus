def do_algebra(operator, operand):
    result = 0
    # Using stack to store the operands and operators separately.
    op_stack = [operator.pop(0)] * len(operand)
    num_stack = operand[:]
    # Iterating to create the expression from the given operands and operators.
    for i in range(len(operand) - 1):
        op = op_stack.pop()
        num1 = num_stack.pop()
        num2 = num_stack.pop()
        num = num1 % num2
        if op == '+':
            num_stack.append(num + num2)
        elif op == '-':
            num_stack.append(num - num2)
        elif op == '*':
            num_stack.append(num * num2)
        elif op == '**':
            num_stack.append(num2 ** num1)
        elif op == '//':
            num_stack.append(num // num2)
        result += num_stack.pop()
    return result