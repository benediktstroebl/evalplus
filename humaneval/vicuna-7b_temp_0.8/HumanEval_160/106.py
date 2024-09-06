
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
    operands = [operand[0]]
    for i in range(1, len(operand)):
        operands.append(operand[i])
    operand = ''.join(str(n) for n in operands)

    expression = ''.join(str(n) for n in operator)
    for i in range(len(expression)):
        if expression[i] == '*':
            a, b = expression[i+1:], expression[0]
            expression = expression[:i] + str(eval(a) * eval(b)) + expression[i+2:]
        elif expression[i] == '/':
            a, b = expression[i+1:], expression[0]
            expression = expression[:i] + str(eval(a) // eval(b)) + expression[i+2:]
        elif expression[i] == '^':
            a, b = expression[i+1:], expression[0]
            expression = expression[:i] + str(eval(a) ** eval(b)) + expression[i+2:]
        else:
            expression = expression[:i] + str(eval(expression[i])) + expression[i+1:]

    result = eval(expression)
    return result