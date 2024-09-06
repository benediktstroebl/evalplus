def do_algebra(operator, operand):
    result = 0
    # Calculate the length of the shorter list to iterate with a single loop
    n = min(len(operator), len(operand))
    for i in range(n):
        result += operand[i] * operator[i]
    # Since the length of the operand list is greater by 1, the last operand is unused.
    result += operand[-1]
    return result