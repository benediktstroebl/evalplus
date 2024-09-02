
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

    operand_list = operand.copy()
    operator_list = operator.copy()
    # If the operator list is empty, raise error
    if len(operator_list) == 0:
        raise ValueError("Operator list is empty")
    # If the operand list is empty, raise error
    if len(operand_list) == 0:
        raise ValueError("Operand list is empty")
    # If the operand list length is one, raise error
    if len(operand_list) == 1:
        raise ValueError("Operand list is empty")

    # If the operator list length is greater than the operand list length, raise error
    if len(operator_list) > len(operand_list) - 1:
        raise ValueError("Operator list is too long")

    # If the operand list length is less than the operator list length, raise error
    if len(operator_list) < len(operand_list) - 1:
        raise ValueError("Operator list is too short")

    # If the operand list contains negative values, raise error
    for i in operand_list:
        if i < 0:
            raise ValueError("Operand list has negative values")

    # If the operator list contains anything other than the basic arithmetic operations, raise error
    for i in operator_list:
        if i not in ['+', '-', '*', '//', '**']:
            raise ValueError("Operator list contains non-arithmetic operations")

    # For the first n-1 numbers in the operand list, take the nth number in the operand list and the nth 
    # operator in the operator list and evaluate them. 
    for i in range(len(operator_list)):
        if operator_list[i] == '+':
            operand_list[i + 1] += operand_list[i]
        elif operator_list[i] == '-':
            operand_list[i + 1] -= operand_list[i]
        elif operator_list[i] == '*':
            operand_list[i + 1] *= operand_list[i]
        elif operator_list[i] == '//':
            operand_list[i + 1] //= operand_list[i]
        elif operator_list[i] == '**':
            operand_list[i + 1] **= operand_list[i]
    
    # Return the final result
    return operand_list[-1]
