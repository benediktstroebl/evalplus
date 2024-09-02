
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
    operands = operand[:-1]
    operator_list = operator[:-1]
    expression = []
    result = 0

    for i in range(len(operands) - 1):
        j = i + 1
        if operator_list[i] == '*':
            expression.append(operands[i] * operands[j])
        elif operator_list[i] == '//':
            expression.append(math.floor(operands[i] / operands[j]))
        else:
            expression.append(operands[i] / operands[j])

    for k in range(len(expression) - 1):
        result = result + expression[k]
        expression.pop(k)

    if expression:
        result = result ** expression.pop()

    return result