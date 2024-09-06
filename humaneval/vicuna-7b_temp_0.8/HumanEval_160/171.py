
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
    operand_length = len(operand)
    if operand_length < 2:
        raise ValueError("Operand list must have at least two operands")

    for operator_index, operator_ in enumerate(operator):
        if operator_index == 0:
            if not operand[0] % 2 == 0:
                raise ValueError("Operand must be an even number")
        elif operator_ == '**':
            if operand[1] < 0:
                raise ValueError("Exponent must be non-negative")
            n = operand[1]
            for i in range(2, operand_length):
                n = n * operand[i]
            for _ in range(n - 1, 0, -1):
                n = n // operator[operator_index + 1]
        elif operator_ == '/':
            if operand[1] == 0:
                raise ValueError("Cannot divide by zero")
            for i in range(2, operand_length):
                if operand[i] == 0:
                    raise ValueError("Cannot divide by zero")
                n = operand[1] // operand[i]
            for _ in range(n - 1, 0, -1):
                n = n // operand[i]
        elif operator_ == '*':
            for i in range(2, operand_length):
                n = operand[1] * operand[i]
            for _ in range(n - 1, 0, -1):
                n = n * operator[operator_index + 1]
        else:
            for i in range(2, operand_length):
                n = operand[1] + operator[operator_index] * operand[i]
            for _ in range(n - 1, 0, -1):
                n = n + operator[operator_index + 1]

    return eval(operator, [0, operand[0]])
