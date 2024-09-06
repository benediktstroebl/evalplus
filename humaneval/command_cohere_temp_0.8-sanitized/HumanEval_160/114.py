def do_algebra(operator, operand):
    result = 0
    Operand = len(operand)
    for i in range(Operand):
        for j in range(i + 1, Operand):
            result += operand[i] * operand[j]
            for k in range(0, Operand):
                if k != i and k != j:
                    result += operand[k]
                    if operator[k] == '+':
                        result //= 2
                        result *= operand[k]
                    elif operator[k] == '-':
                        result //= operand[k]
                    elif operator[k] == '*':
                        result //= operand[k]
                        result *= operand[k]
                    elif operator[k] == '**':
                        result //= operand[k]
                        result *= operand[k]
                    elif operator[k] == '//':
                        result //= operand[k]
    return result