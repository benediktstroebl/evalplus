
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
    # take the first element of operator list
    operator_func = operator[0]
    # take the operand list
    operand_list = operand[:-1]

    # check if the number of elements in operator list is equal to the number of operands in the operand list
    if len(operator) != len(operand_list):
        print("Error: number of operators and operands does not match")
        return None
    # check if the operator is a valid operator
    if not isinstance(operator_func, int):
        print("Error: operator is not a valid operation")
        return None
    # check if the operand is a list of non-negative integers
    if not isinstance(operand_list, list) or not all(map(lambda x: x >= 0, operand_list)):
        print("Error: operand is not a list of non-negative integers")
        return None
    # check if the operator is a valid operator
    if operator_func not in ['+', '-', '*', '/', '**']:
        print("Error: operator is not a valid operation")
        return None
    # check if the operator is a valid operator
    if operator_func == '**':
        # check if the operand is a list of integers
        if not isinstance(operand_list, list) or not all(map(lambda x: x % 1 == 0, operand_list)):
            print("Error: operand is not a list of integers")
            return None
    # check if the operator is a valid operator
    if operator_func == '//':
        # check if the operand is a list of integers
        if not isinstance(operand_list, list) or not all(map(lambda x: x % 1 == 0, operand_list)):
            print("Error: operand is not a list of integers")
            return None
    # check if the operator is a valid operator
    if operator_func == '+':
        # add the operands
        operand_sum = sum(operand_list)
    elif operator_func == '-':
        # subtract the operands
        operand_diff = abs(sum(operand
