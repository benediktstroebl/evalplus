def do_algebra(operator, operand):
    result = 0
    # Use tuple unpacking to assign operator and operand to multiple variables
    ((a, b), op, *rest_op) = ((operator[0], operand[0]), operator[1], operator[2:])
    for n in operand[1:]:
        result += a * n * op(b, n)
        a, b = b, n
    for op in rest_op:
        result += a * op(b, operand[-1])
    return result