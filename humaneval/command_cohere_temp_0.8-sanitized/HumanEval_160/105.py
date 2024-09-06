def do_algebra(operator, operand):
    result = 0
    # Using loop to handle all possible combinations of operands and operators.
    for i in range(len(operand)-1):
        for j in range(i+1, len(operand)):
            # Handling exponentiation with both variables as the base.
            if operator[i] == '**' and operator[j] == '**':
                result += operand[i] ** operand[j]
            # Handling exponentiation with only first variable as the base.
            elif operator[i] == '**':
                result += operand[i] ** operand[j] * operand[i]
            # Handling exponentiation with only second variable as the base.
            elif operator[j] == '**':
                result += operand[i] * operand[j] ** operand[i]
            # Handling all other cases.
            else:
                result += eval(f'{operand[i]}{operator[i]}{operand[j]}')
    return result