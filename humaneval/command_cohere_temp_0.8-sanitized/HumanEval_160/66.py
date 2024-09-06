def do_algebra(operator, operand):
    if len(operator) != len(operand) - 1 or len(operand) < 2 or not all(isinstance(x, int) for x in operand) or not all(x in ['+', '-', '*', '//', '**'] for x in operator):
        raise ValueError("Invalid input format")
    result = 0
    oper_len = len(operator)
    for i in range(oper_len):
        result += operand[i] * operator[i]
    return result