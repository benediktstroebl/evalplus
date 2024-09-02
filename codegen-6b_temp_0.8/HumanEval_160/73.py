
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
    operator_list = operator
    operand_list = operand
    result = 0
    for index in range(len(operator_list)):
        if operator_list[index] == '+':
            result += operand_list[index]
        elif operator_list[index] == '-':
            result -= operand_list[index]
        elif operator_list[index] == '*':
            result *= operand_list[index]
        elif operator_list[index] == '/':
            try:
                result //= operand_list[index]
            except ZeroDivisionError:
                print('division by zero')
                break
        elif operator_list[index] == '**':
            result **= operand_list[index]
    return result
