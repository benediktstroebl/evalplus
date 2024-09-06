
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
    length = len(operator)
    stack = []
    for i, v in enumerate(operand):
        if i == 0:
            stack.append(v)
        else:
            a = stack.pop()
            b = stack.pop()
            if operator[length - 1] == '+':
                stack.append(a + b)
            elif operator[length - 1] == '-':
                stack.append(b - a)
            elif operator[length - 1] == '*':
                stack.append(a * b)
            elif operator[length - 1] == '//':
                stack.append(b // a)
            elif operator[length - 1] == '**':
                stack.append(b ** a)
            length -= 1
            if i == len(operand) - 1:
                return stack.pop()
