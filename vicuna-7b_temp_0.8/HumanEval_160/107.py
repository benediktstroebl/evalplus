
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
    # Operand is a list of integers.
    operand_list = operand[:-1]

    # Determine the type of operator.
    if operator[0] == '+':
        operator = operator[1:]
    elif operator[0] == '-':
        operator = operator[1:]
    elif operator[0] == '*':
        operator = operator[1:]
    elif operator[0] == '//':
        operator = operator[1:]
    elif operator[0] == '**':
        operator = operator[1:]
    else:
        raise ValueError("Invalid operator")

    # Create a new list to store the result.
    result = []

    # Evaluate the expression using the basic algebra operations.
    for i in range(0, len(operator), 2):
        # Evaluate the left and right operands.
        l = operand_list[i]
        r = operand_list[i + 1]

        # Determine the type of the operator.
        op = operator[i]

        # Perform the operator.
        if op == '+':
            result.append(l + r)
        elif op == '-':
            result.append(l - r)
        elif op == '*':
            result.append(l * r)
        elif op == '/':
            if not (r % 1):
                raise ValueError("Cannot divide by zero")
            result.append(l / r)
        elif op == '**':
            result.append(l ** r)

    # Evaluate the result.
    return result[::-1]
