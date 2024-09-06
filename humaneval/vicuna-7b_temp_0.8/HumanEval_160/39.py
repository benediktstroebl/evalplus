
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
    if len(operator) < len(operand):
        raise ValueError("Operator list should have more elements than operand list")
    if not operator:
        raise ValueError("Operator list should contain at least one operator")
    if not operand:
        raise ValueError("Operand list should contain at least two operands")

    operand_index = len(operand)
    result = 0

    for operator_index, operator in enumerate(operator):
        if operator == '*':
            for i in range(operand_index):
                result += operand[i] * operand[i]
        elif operator == '/':
            for i in range(operand_index-1):
                result += operand[i] / operand[i+1]
        elif operator == '+':
            for i in range(operand_index):
                result += operand[i]
        elif operator == '-':
            for i in range(operand_index):
                result -= operand[i]
        elif operator == '**':
            for i in range(operand_index-1):
                result *= operand[i]

    return result
