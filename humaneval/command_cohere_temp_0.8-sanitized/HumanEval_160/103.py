def do_algebra(operator, operand):
    result = 0
    # Handle exponentiation explicitly
    exp_op = operator.pop() if operator and operator[-1] == "**" else None
    for op in operator:
        if op == "+" : result += operand.pop()
        elif op == "-" : result -= operand.pop()
        elif op == "*" : result *= operand.pop()
        elif op == "/" : result //= operand.pop()
        elif exp_op: result = result ** operand.pop()
        else: return "Error! Invalid operator %s in the list of operators!" % op
    return result