
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

    # 1. convert the operator to a list of (operator, operand)
    # 2. evaluate the (operator, operand) until only one operand left

    # 1.
    operands = operand.copy()
    opers = []
    for i in range(len(operator)):
        opers.append((operator[i], operands[i], operands[i+1]))
        operands.pop(i)
        operands.pop(i)
    # print(opers)

    # 2.
    result = opers[0][1]
    # print(result)
    for i in range(1, len(opers)):
        if opers[i][0] == '+':
            result += opers[i][2]
        elif opers[i][0] == '-':
            result -= opers[i][2]
        elif opers[i][0] == '*':
            result *= opers[i][2]
        elif opers[i][0] == '//':
            result //= opers[i][2]
        elif opers[i][0] == '**':
            result **= opers[i][2]
    print(result)
    return result
