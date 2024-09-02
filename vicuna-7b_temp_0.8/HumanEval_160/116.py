
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
    operand = list(operand)
    if len(operator) < len(operand):
        raise ValueError("Operator list is too short")
    if not any(op >= 0 for op in operator):
        raise ValueError("Operand list should contain only non-negative integers")
    for i, op in enumerate(operator):
        if i == 0 and not any(op >= 0 for op in operand):
            raise ValueError("Operand list should contain only non-negative integers")
        if op not in ['+', '-', '*', '/']:
            raise ValueError("Invalid operator")
        if not isinstance(operand[i], int):
            raise ValueError("Operand should contain integers")
    result = 0
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i]
        elif operator[i] == '-':
            result -= operand[i]
        elif operator[i] == '*':
            result *= operand[i]
        elif operator[i] == '/':
            if not isinstance(operand[i+1], int):
                raise ValueError("Cannot divide by non-integer")
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result
