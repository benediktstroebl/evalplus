
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
    result = 0
    num_operands = len(operand)
    num_operators = len(operator)
    for i in range(num_operands):
        for j in range(1, num_operators):
            expression = operator[j]
            operand_index = i
            if expression == '*':
                result = result * operand[operand_index]
            elif expression == '/':
                result = result / operand[operand_index]
            elif expression == '+':
                result = result + operand[operand_index]
            elif expression == '-':
                result = result - operand[operand_index]
            else:
                result = result * operand[operand_index] ** operator[j]
    return eval(expression)