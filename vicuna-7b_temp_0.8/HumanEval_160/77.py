
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
    operand_len = len(operand)
    if operator[0][0] == '**':
        raise ValueError("Invalid operator")
    if len(operator) != operand_len:
        raise ValueError("Invalid operator")
    for i in range(0, operand_len):
        if operator[i][0] == '+':
            expr = operand[i]
        elif operator[i][0] == '-':
            expr = operand[i]
        elif operator[i][0] == '*':
            expr = operand[i]
        elif operator[i][0] == '//':
            expr = operand[i]
        elif operator[i][0] == '-':
            expr = operand[i]**-1
        else:
            raise ValueError("Invalid operator")
        for j in range(i+1, len(operator)):
            if operator[j][0] == '+':
                expr = expr + operand[j]
            elif operator[j][0] == '-':
                expr = expr - operand[j]
            elif operator[j][0] == '*':
                expr = expr * operand[j]
            else:
                raise ValueError("Invalid operator")
    return expr
