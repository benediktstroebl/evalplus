
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
    operands = operand[1:]
    for i in range(0, len(operand) - len(operator[0])):
        evaluation = []
        for j in range(len(operator)):
            if i == j:
                evaluation.append(0)
            else:
                evaluation.append(operator[i])
        result = eval(evaluation)
        for k in range(len(operand) - len(operator[0])):
            if operand[0] == operand[1]:
                operand[0] += result
            else:
                operand[0] = operator[i]
                operand[1] = operand[1] - result
    return operand[0]