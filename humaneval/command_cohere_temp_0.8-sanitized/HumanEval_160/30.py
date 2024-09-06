def do_algebra(operator, operand):
    num_operands = len(operand)
    expr = []
    for i in range(num_operands - 1):
        expr.append(operand[i])
        for j in range(i + 1, num_operands):
            if operator[i] == "+":
                expr.append(operand[j])
            elif operator[i] == "-":
                expr.append(operator[i] + "(" + operand[j] + " - " + operand[i] + ")")
            elif operator[i] == "*":
                expr.append(operator[i] + "(" + operand[j] + " * " + operand[i] + ")")
            elif operator[i] == "//":
                expr.append(operator[i] + "(" + operand[j] + " // " + operand[i] + ")")
            elif operator[i] == "**":
                expr.append(operator[i] + "(" + operand[j] + " ** " + operand[i] + ")")
    return expr[0] + " " + expr[1:]