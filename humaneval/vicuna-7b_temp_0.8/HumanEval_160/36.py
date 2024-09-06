
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
    expression = operator[0]
    for i in range(1, len(operator)):
        operator = operator[i]
        for j in range(len(operand)):
            if j == 0 or j == len(operand) - 1:
                expression = operator * expression
            else:
                expression = expression * operator
    result = expression
    for i in range(len(operand)):
        result = result / operand[i]
    return result

if __name__ == '__main__':
    print(do_algebra('+', [3, 2, 1]))
    print(do_algebra('*', [1, 2, 3, 4, 5]))
    print(do_algebra('/', [10, 5, 2, 1]))
    print(do_algebra('**', [2, 3, 4, 5, 6]))
    print(do_algebra('-', [2, 3, 4, 5]))