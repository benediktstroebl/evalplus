
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
    # Operand has to be non-negative
    if any(n < 0 for n in operand):
        raise ValueError("Operand has to be non-negative")
    
    # Operator list has to be greater than or equal to 1
    if len(operator) == 0:
        raise ValueError("Operator list has to be greater than or equal to 1")

    # Operator and operand lists have to be the same length
    if len(operator) + 1!= len(operand):
        raise ValueError("Operator and operand lists have to be the same length")

    # Basic algebra operations
    basic_operations = {
        '+': operator.index('+'),
        '-': operator.index('-'),
        '*': operator.index('*'),
        '//': operator.index('//'),
        '**': operator.index('**')
    }

    for operation in basic_operations:
        if operation in operator:
            try:
                operator_index = basic_operations[operation]
            except ValueError:
                raise ValueError("Operator list does not contain valid operation")
            else:
                left_operand = operand[:operator_index]
                right_operand = operand[operator_index + 1:]

                # Addition
                if operation == '+':
                    return add(left_operand, right_operand)

                # Subtraction
                if operation == '-':
                    return subtract(left_operand, right_operand)

                # Multiplication
                if operation == '*':
                    return multiply(left_operand, right_operand)

                # Floor division
                if operation == '//':
                    return floor_divide(left_operand, right_operand)

                # Exponentiation
                if operation == '**':
                    return power(left_operand, right_operand)

