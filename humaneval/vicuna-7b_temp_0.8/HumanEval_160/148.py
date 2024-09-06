
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
    operator_index = 0
    result = operand[0]
    for index in range(1, len(operand)):
        operator = operator[operator_index]
        operator_index += 1
        operand_index = 0
        for i in range(1, len(operands)):
            if operands[i] == operand[i]:
                operand_index += 1
                if operand_index == len(operands):
                    break
            elif operand[i] % 2 == 0:
                result = operator(result, operands[i])
                operand_index += 1
            elif operator == '**':
                result = operator(result, operands[i])
                operand_index += 1
                result = result * operand[i]
                operand_index += 1
                break
            else:
                result = operator(result, operands[i])
                operand_index += 1
    return result