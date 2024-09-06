def do_algebra(operator, operand):
    result = 0
    # Handle exponentiation separately, as it needs to be iterated through
    # the lists in a different manner than the other operations
    if "**" in operator:
        for op in operand:
            result = result * op
    else:
        # Assuming the length of operand list is greater than or equal to the length of operator list
        for i in range(len(operand) - 1):
            result = result + operand[i] if operator[i] == "+" else result - operand[i] if operator[i] == "-" else result * operand[i]
        result = result // operand[-1] if "//" in operator else result ** operand[-1]
    return result