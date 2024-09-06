def do_algebra(operator, operand):
    result = 0
    # Calculate result using python eval function
    for i in range(len(operand)-1):
        temp = list(operand[i])
        for j in range(i+1, len(operand)):
            temp.extend(str(operand[j]))
            temp = ' '.join(temp)
            result += eval(f'{operator[i]}{temp}')
    return result