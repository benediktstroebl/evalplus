def do_algebra(operator, operand):
    result = 0
    # Calculate sum when the operator is +
    if operator[0] == '+':
        result += operand[0]
    # Calculate difference when the operator is -
    if operator[0] == '-':
        result -= operand[0]
    # Calculate product when the operator is *
    if operator[0] == '*':
        result *= operand[0]
    # Calculate floor division when the operator is // (Dev note: added explicit checking for floor division)
    if operator[0] == '//':
        result //= operand[0]
    # Calculate exponentiation when the operator is **
    if operator[0] == '**':
        result **= operand[0]
    return result