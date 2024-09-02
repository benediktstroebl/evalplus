
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
    operands = operand[1:]
    # Check if the operator is the correct type
    if not all(isinstance(op, str) for op in operator):
        return None
    if len(operator) != len(operand[0]) - 1:
        return None
    # Check if the operator is valid on the operands
    operand_length = len(operand)
    for i in range(0, operand_length, 2):
        # if operator[0] == operator[1]
        if operator[0] == operator[1] and operator[0] in ['-', '+']:
            # Check if the operand is negative
            if operand[i] < 0:
                return -eval(operator[0] + str(int(operator[1]) * abs(operand[i])))
            else:
                return eval(operator[0] + str(int(operator[1]) * operand[i]))
        elif operator[0] == operator[1] and operator[0] == '*':
            # Check if the operand is negative
            if operand[i] < 0:
                return -eval(operator[0] + str(int(operator[1]) * abs(operand[i])))
            else:
                return eval(operator[0] + str(int(operator[1]) * operand[i]))
        else:
            raise ValueError("Invalid operator")
    # Check if the operator is valid
    if operator[0] == '**':
        for i in range(1, len(operator)):
            if not isinstance(operator[i], str):
                return None
        return eval(operator[0] + str(int(operator[1]) * eval(operator[2])))
    raise ValueError("Invalid operator")
