
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
    # solution 1
    # operand = list(map(int, operand))
    # # operator_dict = {'+': operator.__add__, '-': operator.__sub__, '*': operator.__mul__, '/': operator.__floordiv__, '**': operator.__pow__}
    # operator_dict = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x // y, '**': lambda x, y: x ** y}
    # for i, op in enumerate(operator):
    #     for j in range(1, len(operand)):
    #         operand[j] = operator_dict[op](operand[j], operand[j - 1])
    #         operand.pop(0)
    # return operand[0]

    # solution 2
    operand = list(map(int, operand))
    operator_dict = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x // y, '**': lambda x, y: x ** y}
    for i, op in enumerate(operator):
        operand[i + 1] = operator_dict[op](operand[i], operand[i + 1])
    return operand[i + 1]
