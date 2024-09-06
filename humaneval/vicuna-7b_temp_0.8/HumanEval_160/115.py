
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
    operand = list(operand)
    result = operator[0]
    for i in range(1, len(operator)):
        operator_op = operator[i]
        operand_operand = operand[-1]
        for j in range(i, len(operator)):
            operator_next_op = operator[j]
            operand_mul = operand_operand ** operator_next_op
            if operator_op == '+':
                result = result + operand_mul
            elif operator_op == '-':
                result = result - operand_mul
            elif operator_op == '*':
                result = result * operand_mul
            elif operator_op == '//':
                result = result // operand_mul
            elif operator_op == '**':
                result = result ** operand_mul
            operand = operand[:-1]
    return result
