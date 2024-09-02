
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
    # print(operator, operand)
    if len(operand) == 1:
        return operand[0]
    if len(operator) == 1:
        if operator[0] == '+':
            return operand[0] + operand[1]
        elif operator[0] == '-':
            return operand[0] - operand[1]
        elif operator[0] == '*':
            return operand[0] * operand[1]
        elif operator[0] == '/':
            return operand[0] // operand[1]
        elif operator[0] == '**':
            return operand[0] ** operand[1]
    else:
        for i in range(len(operator)):
            if operator[i] == '+':
                operand[0] += operand[i+1]
            elif operator[i] == '-':
                operand[0] -= operand[i+1]
            elif operator[i] == '*':
                operand[0] *= operand[i+1]
            elif operator[i] == '/':
                operand[0] //= operand[i+1]
            elif operator[i] == '**':
                operand[0] **= operand[i+1]
            # print(operand, operand[0])
        return operand[0]


