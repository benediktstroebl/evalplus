def do_algebra(operator, operand):
    result = 0
    # Using loop to avoid nested loops
    for i in range(len(operand)-1):
        # Using parallelogram law to avoid nested loops
        for j in range(i+1, len(operand)):
            result += operand[i] * operand[j] * operator[i-j]
    return result