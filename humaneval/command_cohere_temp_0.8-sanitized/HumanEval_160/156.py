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
    num_operands = len(operand)
    expr_list = [operand[i] for i in range(num_operands - 1)]
    for i in range(num_operands - 1):
        operator_token = operator[i % len(operator)]
        if operator_token == '*':
            expr_list.append(expr_list[i] * expr_list[i + 1])
        elif operator_token == '+':
            expr_list.append(expr_list[i] + expr_list[i + 1])
        elif operator_token == '-':
            expr_list.append(expr_list[i] - expr_list[i + 1])
        elif operator_token == '**':
            expr_list.append(expr_list[i] * expr_list[i + 1])
        elif operator_token == '/':
            expr_list.append(expr_list[i] // expr_list[i + 1])
    return expr_list[-1]