
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
    # Using recursive to solve the problem.
    # TODO: use recursive to solve the problem.
    # Return the result.
    
    if not operator:
        return operand[0]

    operator_list = operator[-1]
    operand_list = operand[:-1]

    # left_operand = operand_list[0]
    # right_operand = operand_list[1]
    
    if operator_list == '+':
        return do_algebra(operator[:-1], [operand_list[0] + operand_list[1]])
    elif operator_list == '-':
        return do_algebra(operator[:-1], [operand_list[0] - operand_list[1]])
    elif operator_list == '*':
        return do_algebra(operator[:-1], [operand_list[0] * operand_list[1]])
    elif operator_list == '//':
        return do_algebra(operator[:-1], [operand_list[0] // operand_list[1]])
    elif operator_list == '**':
        return do_algebra(operator[:-1], [operand_list[0] ** operand_list[1]])
    else:
        print("Unsupported operator")
        return None

