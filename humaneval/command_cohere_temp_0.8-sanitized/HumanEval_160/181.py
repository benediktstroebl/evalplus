def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
       The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.
    """
    num_operands = len(operand)
    if num_operands == 1:
        raise ValueError("Operand list must have at least two integers")
    
    num_operators = len(operator)
    if num_operators == 0:
        raise ValueError("Operator list must have at least one operator")
    
    expression_parts = []
    for i in range(num_operands):
        part = operand[i]
        for j in range(i + 1, num_operands):
            operator_token = operator[j - i - 1]
            part = operate(operator_token, part, operand[j])
            if part == 0:
                break
        expression_parts.append(part)
    
    return expression_parts[0]
def operate(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    if operator == '-':
        return operand1 - operand2
    if operator == '*':
        return operand1 * operand2
    if operator == '//':
        return operand1 // operand2
    if operator == '**':
        return operand1 ** operand2
operand = [2, 3, 4, 5]
operator = ['+', '*', '-']