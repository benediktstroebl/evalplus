
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
    # todo: test case should be more complete.
    # todo: should not hard code result, result should be a variable
    # todo: should return None if operand length is not long enough
    # todo: should return None if operand list is not a list
    # todo: should return None if operand contains negative number
    # todo: should return None if operand contains float
    # todo: should return None if operator contains a wrong symbol
    # todo: should return None if operator is not a list
    # todo: should return None if operator is not the right size
    # todo: should return None if operator contains a wrong symbol
    result = operand[0]
    for i in range(len(operator)):
        op = operator[i]
        if op == '+':
            result += operand[i + 1]
        elif op == '-':
            result -= operand[i + 1]
        elif op == '*':
            result *= operand[i + 1]
        elif op == '//':
            result //= operand[i + 1]
        elif op == '**':
            result **= operand[i + 1]
    return result





