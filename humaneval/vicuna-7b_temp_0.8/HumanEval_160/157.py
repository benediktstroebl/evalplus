
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
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator list must have the same length as operand list minus one")
    if not operator:
        raise ValueError("Operator list must contain at least one operator")
    if not operand:
        raise ValueError("Operand list must contain at least two operands")
    if not all(x >= 0 for x in operand):
        raise ValueError("Operand list must contain only non-negative integers")
    
    operand_copy = operand.copy()
    operand_tuple = tuple(operand_copy)
    if operator[0] == '*':
        result = 1
    else:
        result = operator[0]
    for i in range(1, len(operator)):
        operator_i = operator[i]
        if operator_i == '+':
            operator_i_val = operand_tuple[i-1] + operand_tuple[i]
            result = operator_i_val
        elif operator_i == '-':
            operator_i_val = operand_tuple[i-1] - operand_tuple[i]
            result = operator_i_val
        elif operator_i == '*':
            operator_i_val = operand_tuple[i-1] * operand_tuple[i]
            result = operator_i_val
        elif operator_i == '//':
            operator_i_val = int(operand_tuple[i-1]) // int(operand_tuple[i])
            result = operator_i_val
        elif operator_i == '**':
            operator_i_val = math.pow(operand_tuple[i-1], int(operand_tuple[i]))
            result = operator_i_val
        else:
            raise ValueError("Invalid operator")
    return result
