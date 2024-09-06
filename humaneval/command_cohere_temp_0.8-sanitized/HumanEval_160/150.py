def do_algebra(operator, operand):
    result = 0
    # Calculate result using eval function
    for i in range(len(operand)-1):
        temp = operand[i]
        for j in range(i+1, len(operand)):
            temp = temp * 1
            if operator[i] == '+':
                temp += operand[j]
            elif operator[i] == '-':
                temp -= operand[j]
            elif operator[i] == '*':
                temp *= operand[j]
            elif operator[i] == '//':
                temp //= operand[j]
            elif operator[i] == '**':
                temp **= operand[j]
            result += temp
    return result