
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
    operand_index = len(operand) - 1
    left_result = []
    right_result = []

    for operator_index, operator in enumerate(operator):
        if operator == '*':
            for i in range(operand_index, len(operand)):
                left_result.append(operand[i-1])
            left_result.append(operand[operand_index])
            for i in range(operand_index+1, len(operand)):
                right_result.append(operand[i])
            right_result.append(operand[operand_index-1])
            result = left_result + right_result
            for i in range(operand_index-1, -1, -1):
                result.append(0)
        elif operator == '/':
            for i in range(operand_index, len(operand)):
                left_result.append(operand[i-1])
            left_result.append(operand[operand_index])
            for i in range(operand_index+1, len(operand)):
                right_result.append(0)
                right_result.append(operand[i])
            result = left_result + right_result
            for i in range(operand_index-1, -1, -1):
                result.append(0)
        elif operator == '**':
            for i in range(operand_index, len(operand)):
                left_result.append(operand[i-1])
            left_result.append(operand[operand_index])
            for i in range(operand_index+1, len(operand)):
                right_result.append(operand[i])
            result = left_result ** right_result
            for i in range(operand_index-1, -1, -1):
                result.append(0)
        elif operator == '-':
            for i in range(operand_index, len(operand)):
                left_result.append(operand[i-1])
            left_result.append(0)
            for i in range(operand_index+1
