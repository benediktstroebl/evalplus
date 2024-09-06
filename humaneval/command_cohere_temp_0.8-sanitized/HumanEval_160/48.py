def do_algebra(operator, operand):
    result = 0
    # Using loop to handle all possible combinations of operands and operators.
    for i in range(len(operand)-1):
        for j in range(i+1, len(operand)):
            # Different operand types handling.
            if operator[i] == '*' or operator[j] == '*':
                result += operand[i] * operand[j]
            # Handling Floor Division
            if operator[i] == '/' or operator[j] == '/':
                result += operand[i] // operand[j]
            # Handling Addition and Subtraction
            if (operator[i] == '+' or operator[i] == '-') and (operator[j] == '+' or operator[j] == '-'):
                result += operand[i] % 10 * pow(10, operand[j] % 10)
                result += ((operand[j] - operand[i]) % 10) * pow(10, (operand[j] // 10 - operand[i] // 10))
            # Handling Exponentiation
            if operator[i] == '^' or operator[j] == '^':
                result += pow(operand[i], operand[j])
    return result