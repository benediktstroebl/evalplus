
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
    operands = operand[1:] # removing the operand from operand list
    result = operand[0]
    for index in range(1, len(operand)):
        operator = operator[index]
        operand = operand[index+1]
        if operator == '*':
            result = eval_mul(result, operand)
        elif operator == '/':
            result = eval_div(result, operand)
        elif operator == '**':
            result = eval_pow(result, operand)
        elif operator == '+':
            result = eval_add(result, operand)
        elif operator == '-':
            result = eval_sub(result, operand)
    return eval_expr(result)
