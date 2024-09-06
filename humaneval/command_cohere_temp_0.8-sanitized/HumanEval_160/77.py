def do_algebra(operator, operand):
    result = 0
    # Using loop to handle multiple elements in the operation
    for i in range(len(operand)):
        for oper in operator:
            # Handling exponentiation
            if oper == "**":
                result = result * operand[i] ** oper
              # Handling rest of the operations
            else:
                result = result * oper(operand[i])
    return result