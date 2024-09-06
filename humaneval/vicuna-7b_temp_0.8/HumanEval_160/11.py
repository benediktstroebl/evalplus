
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
    operands = [operand]
    operator = operator.split()
    operator = [op[0] for op in operator]
    operator = [i if i in ['/', '**'] else i - 1 for i in operator]
    operator = [int(i) if i.isdigit() else i for i in operator]

    # Check if the operator is a legal operator for the given operand
    if operator[-1] == operator[0] % 2 == 0:
        raise ValueError(f"Invalid operator {operator[-1]} for operand {operand}")

    # Initialize the result to the empty list
    result = []

    for i, op in enumerate(operator):
        # Check if the operand matches the type of the operator
        if op == '*':
            if i < len(operand) - 1:
                # Multiply the two previous operands
                result.append(operand[i] * operand[i + 1])
        elif op == '/':
            # Floor division
            if i < len(operand) - 1:
                quotient = operand[i + 1]
                remainder = operand[i]
                result.append(quotient)
            else:
                result.append(operand[i])
        elif op == '**':
            if i < len(operand) - 1:
                # Raise the two previous operands to the power
                result.append(operand[i] ** operand[i + 1])
        else:
            # Addition, subtraction
            if i < len(operand) - 1:
                # Addition or subtraction
                result.append(operand[i] + operand[i + 1])
        operands.append(result[-1])

    return operands