def do_algebra(operator, operand):
    num_operands = len(operand)
    expression = []
    for i in range(num_operands - 1):
        cur_op = operator[i % len(operator)]
        cur_operand = operand[i]
        next_operand = operand[(i + 1) % num_operands]
        expression.append(f'{cur_operand}{cur_op}{next_operand}' if cur_operand != '0' else cur_operand)
    
    return sum(eval(x) for x in expression)