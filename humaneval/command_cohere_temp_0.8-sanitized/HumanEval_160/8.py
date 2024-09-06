def do_algebra(operator, operand):
    """
    Evaluates an algebraic expression built from the given operator and operand.
    """
    # Ensure proper lengths of operator and operand
    assert len(operator) == len(operand) - 1, "Operator and operand lengths must match."
    
    # Algorithm
    result = 0
    for i in range(len(operand) - 1):
        result += operand[i]
        for j in range(len(operator)):
            if operator[j] == '+':
                result += operand[i + 1]
            elif operator[j] == '-':
                result -= operand[i + 1]
            elif operator[j] == '*':
                result *= operand[i + 1]
            elif operator[j] == '**':
                result **= operand[i + 1]
            elif operator[j] == '/':
                if operand[i + 1] == 0:
                    raise ZeroDivisionError("Floor division by zero is not allowed.")
                result //= operand[i + 1]
    return result