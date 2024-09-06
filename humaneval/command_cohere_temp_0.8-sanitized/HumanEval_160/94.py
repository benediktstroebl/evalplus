def do_algebra(operator, operand):
    num_operands = len(operand)
    expr_list = []
    for i in range(num_operands):
        for j in range(i + 1, num_operands):
            expr_list.append(operand[i] * operator[j - i - 1] + operand[j])
    return expr_list[0]
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]