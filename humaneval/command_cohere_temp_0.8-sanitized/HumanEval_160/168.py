def do_algebra(operator, operand):
    result = 0
    opera_len = len(operator)
    it = iter(operand)
    for i in range(opera_len):
        result += next(it) * eval(f'{operator[i]}{result}')
    return result
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]