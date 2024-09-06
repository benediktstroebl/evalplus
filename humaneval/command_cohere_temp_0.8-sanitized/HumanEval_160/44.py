def do_algebra(operator, operand):
    result = 0
    # Using collections.Counter to conveniently iterate over unique operands with their counts
    op_count = collections.Counter(operand)
    for op in operator:
        result += op_count[op] * operand.count(op)
    return result