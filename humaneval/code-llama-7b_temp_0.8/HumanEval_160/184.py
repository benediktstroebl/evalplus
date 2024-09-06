
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
    print(operator, operand)
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def floor_division(x, y):
        return x // y
    def exponentiation(x, y):
        return x ** y

    operator_dictionary = {
        '+' : add,
        '-' : subtract,
        '*' : multiply,
        '//' : floor_division,
        '**' : exponentiation,
    }
    operator_length = len(operator)
    operand_length = len(operand)
    result = operand[0]
    for i in range(operator_length):
        result = operator_dictionary[operator[i]](result, operand[i+1])
    return result
