def do_algebra(operator, operand):
    result = 0
    # Ensure that the lengths of the two lists are the same, and that they are of different lengths than the result
    assert len(operator) == len(operand) - 1 and len(operand) > 1 and len(result) != len(operator), "Operands and operators lengths must match, and result length must be different"
    # Iterate through the operand list and systematically apply the operators in the order they appear in the operator list
    for i in range(len(operand)):
        for j in range(len(operator)):
            if operator[j] == '+':
                result += operand[i]
            if operator[j] == '-':
                result -= operand[i]
            if operator[j] == '*':
                result *= operand[i]
            if operator[j] == '**':
                result **= operand[i]
            if operator[j] == '/':
                result //= operand[i]
    return result