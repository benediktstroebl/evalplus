
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
    operand = [i for i in operand if i >= 0]  # filter out negative numbers
    if not operator or not operand or len(operator) != len(operand)-1:
        return None

    # evaluate the expression
    expression = []
    for i, operator in enumerate(operator):
        if operator == '*':
            expression.append(sum(map(lambda x: x**i, operand)))
        elif operator == '/':
            expression.append(reduce(lambda x, y: x*y if y % 1 == 0 else x, operand))
        elif operator == '+':
            expression.append(sum(map(lambda x: x if x >= 0 else 0, operand)))
        elif operator == '-':
            expression.append(sum(map(lambda x: x if x >= 0 else 0, operand)))
        else:
            return None
    result = expression[0]
    for i in range(1, len(expression)):
        if expression[i] > 0:
            result *= expression[i]
        else:
            result -= expression[i]
    return result
