
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
    operand_val = operand[0]

    for i in range(len(operator)):
        operator_val = operator[i][0]
        operator_op = operator[i][1]
        operand_val = apply_operator(operator_val, operand_val, operator_op)

    expression = operand_val
    for i in range(len(operands)):
        expression = apply_operator(operator[i][0], expression, operator[i][1])

    return expression
