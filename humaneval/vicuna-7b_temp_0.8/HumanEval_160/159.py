
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
    operand = [int(x) for x in operand]
    operator_len = len(operator[0])
    result = 0

    if operator[0] == '0':
        if operator[1] == 'x':
            return 0
        elif operator[0] == '+':
            for i in range(operator_len, len(operator)):
                operand[0] = operand[0] + operand[i]
        elif operator[0] == '-':
            for i in range(operator_len, len(operator)):
                operand[0] = operand[0] - operand[i]
        elif operator[0] == '*':
            for i in range(operator_len, len(operator)):
                operand[0] = operand[0] * operand[i]
        elif operator[0] == '/':
            for i in range(operator_len, len(operator)):
                operand[0] = operand[0] // operand[i]
        elif operator[0] == '**':
            for i in range(operator_len, len(operator)):
                operand[0] = operand[0] ** operand[i]

    if operator[0] == '1':
        for i in range(operator_len, len(operator)):
            result = result + operand[i]

    if operator[0] == 'x':
        return result % 1

    if operator[0] == '2':
        return result

    return result