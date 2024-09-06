def do_algebra(operator, operand):
    num_operands = len(operand)
    expression = []
    for i in range(num_operands):
        if i > 0:
            expression.append(operator[i-1])
        expression.append(operand[i])
    return evaluate_expression(expression)
def evaluate_expression(expression):
    result = expression[0]
    for i in range(1, len(expression)):
        operator = expression[i]
        if operator == '+':
            result += expression[i+1]
        elif operator == '-':
            result -= expression[i+1]
        elif operator == '*':
            result *= expression[i+1]
        elif operator == '//':
            result //= expression[i+1]
        elif operator == '**':
            result **= expression[i+1]
    return result
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]