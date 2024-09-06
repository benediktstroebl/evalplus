
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
    # a = operator[0]
    # b = operand[0]
    # c = operand[1]
    # d = operator[1]
    # return a + b * c - d
    # print(operator)
    # print(operand)
    operator_list = []
    operand_list = []
    for i in operator:
        if i == '+':
            operator_list.append(i)
            operand_list.append(operand[0])
            operand[0] = 0
        elif i == '-':
            operator_list.append(i)
            operand_list.append(operand[0])
            operand[0] = 0
        elif i == '*':
            operator_list.append(i)
            operand_list.append(operand[0])
            operand[0] = 0
        elif i == '//':
            operator_list.append(i)
            operand_list.append(operand[0])
            operand[0] = 0
        elif i == '**':
            operator_list.append
