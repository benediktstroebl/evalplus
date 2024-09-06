def do_algebra(operator, operand):
    result = 0
    # Using loop to handle all possible combinations of operands and operators
    for i in range(len(operand)-1):
        for j in range(i+1, len(operand)):
            # Handling exponentiation operation
            if operator[i] == '**':
                result += operand[j] ** operand[i]
            # Handling all other operations
            else:
                result += operand[j] * operate(operator[i], operand[i], operand[j])
    return result
def operate(operator, operand1, operand2):
    # Handling Addition
    if operator == '+':
        return operand1 + operand2
    # Handling Subtraction
    if operator == '-':
        return operand1 - operand2
    # Handling Multiplication
    if operator == '*':
        return operand1 * operand2
    # Handling Floor Division
    if operator == '//':
        return operand1 // operand2
    else:
        return 0