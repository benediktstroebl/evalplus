
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
    operand = [i for i in operand if i >= 0]
    if len(operator) == len(operand) - 1:
        result = 0
        for i in range(len(operator)):
            operator_index = operator[i]
            operand_index = operand[i]
            operator_value = operator_index[0]
            operator_type = operator_index[1]
            operator_result = eval(f'{operator_value}{operator_type} {operand_index}')
            result = result + operator_result
        return result
    else:
        return 0

