
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
    if len(operator) == 1:
        operator = [operator[0] for i in range(len(operand) - 1)]
    operator = operator[::-1]
    operand = operand[::-1]
    
    if (len(operator) + 1) == len(operand):
        for i in range(len(operator)):
            try:
                operand[i] = operator[i](operand[i], operand[i + 1])
                del operand[i + 1]
                del operator[i]
            except:
                return operator[0](operand[0], operand[1])
        return operator[0](operand[0], operand[1])

    elif (len(operator) + 1) > len(operand):
        return operator[0](operand[0], operand[1])
    else:
        return operator[0](operand[0], operand[1])
