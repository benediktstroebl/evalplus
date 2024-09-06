def do_algebra(operator, operand):
    result = 0
    # Handle exponentiation explicitly
    exp_op = operator.pop() if operator else None
    if exp_op:
        operand = [x ** y for x, y in zip(operand, operator)]

    for op in operator:
        result += operand[0] * algebra[op]
        operand = operand[1:]

    # If there was an exponentiation operator, handle it now
    if exp_op:
        result += operand[0] if operand else 0
    return result
algebra = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '//': lambda x, y: x // y if y != 0 else float('inf'),
    '**': lambda x, y: x ** y
}