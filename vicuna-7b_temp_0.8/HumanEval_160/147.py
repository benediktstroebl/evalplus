
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
    operator = [int(op) for op in operator]
    if len(operator) < len(operand) - 1:
        return None

    operator = sorted(operator)
    operand = sorted(operand)

    expression = []
    for i in range(0, len(operator), 2):
        op = operator[i]
        a = operand[i]
        expression.append(op)
        expression.append(a)
        if operator[i+1] == '*':
            expression.append('*')
        elif operator[i+1] == '/':
            expression.append('/')
        else:
            expression.append('**')

    # convert expression to string
    expression_str = ''.join(expression)

    result = None
    for j in range(0, len(expression_str), 2):
        op = expression_str[j]
        a = expression_str[j+1]
        if op == '+':
            result = a + result
        elif op == '-':
            result = a - result
        elif op == '*':
            result = a * result
        elif op == '/':
            if a == 0:
                return None
            result = a / result
        elif op == '**':
            result = math.pow(a, result)

    return result
