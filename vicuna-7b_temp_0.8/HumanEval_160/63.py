
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
    operands = [operand[0]]
    if len(operand) < 2:
        raise ValueError("Operand list is too short")
    
    for i in range(1, len(operand)):
        operand_index = int(operator[i])
        operator_index = int(operator[i+1])
        operand_index = int(operand[i])
        operand = [x if x >= 0 else 0 for x in operand[i+1:]]
        operand = [x*operand_index if x == operand_index else x for x in operand]
        operand = [x//operand_index if x % operand_index == 0 else x for x in operand]
        result = operator[operator_index]
        for j in range(len(operand)):
            result = result*operand[j]
        operands.append(result)
    return operands[0]
