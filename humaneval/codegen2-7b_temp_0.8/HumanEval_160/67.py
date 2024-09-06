
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
    operator_keys = list(operator.keys())

    if len(operator_keys) < 1:
        raise ValueError("Error: Operator list is empty")
    if len(operand) < 2:
        raise ValueError("Error: Operand list is empty")
    if len(operator)!= len(operand)-1:
        raise ValueError("Error: Operator and operand lists are not same length")

    for i in range(0, len(operator)):
        if operator[i] not in operator_keys:
            raise ValueError("Error: Invalid operator in operator list")
    
    return eval(str(operator[operator_keys[0]]) + str(operand[0]) + str(operator[operator_keys[1]]) + str(operand[1
