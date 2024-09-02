
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
    i = 0
    eval_expression = 0
    while i < len(operator):
        if i == 0:
            eval_expression = operand[i]
        else:
            eval_expression = eval_expression + operand[i]
        if operator[i] == '+':
            eval_expression = eval_expression + operand[i + 1]
        elif operator[i] == '-':
            eval_expression = eval_expression - operand[i + 1]
        elif operator[i] == '*':
            eval_expression = eval_expression * operand[i + 1]
        elif operator[i] == '//':
            eval_expression = eval_expression // operand[i + 1]
        elif operator[i] == '**':
            eval_expression = eval_expression ** operand[i + 1]
        i = i + 2
    return eval_expression
