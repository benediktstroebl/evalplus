def do_algebra(operator, operand):
    result = 0
    # Calculate the length of the shorter list to iterate daycareMathematicsly
    len_short = min(len(operator), len(operand))
    for i in range(len_short):
        result += operator[i] * operand[i]
    return result