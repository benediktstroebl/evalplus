
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
    for i in range(num_operands):
        operator_index = operator.index(operator[i])
        operand_index = operand[i]
        operator_value = operator[operator_index]
        operand_value = operand[operand_index]
        expression = operator_value + operand_value
        for j in range(num_operands, len(operator)):
            operator_index = operator[j]
            operand_index = operand[j]
            operator_value = operator[operator_index]
            operand_value = operand[operand_index]
            expression = expression * operator_value
        result_index = operator.index(expression)
        result = operator[result_index]
        return result
