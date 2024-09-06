def do_algebra(operator, operand):
    result = 0
    # Calculate result using chained operations
    for i in range(len(operand) - 1):
        result = result + operand[i]
        for j in range(i + 1, len(operand)):
            result = result * 10 ** operand[j]
            if operator[i] == '-':
                result = result - operand[j]
            elif operator[i] == '/':
                result = result // operand[j]
            elif operator[i] == '*':
                result = result * operand[j]
    return result