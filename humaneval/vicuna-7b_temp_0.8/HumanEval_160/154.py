
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
    operand_length = len(operand)
    operator_length = len(operator)
    operand_index = 0

    if operator_length == 0:
        raise ValueError("operator list is empty")

    if operand_length == 1:
        raise ValueError("operand list is empty")

    for i in range(operator_length):
        if operator[i] == '**':
            result = operand[operand_index]
            operand_index += 1
            for j in range(operator[i+1]):
                result = result ** operand[operand_index]
                operand_index += 1
            return result
        elif operator[i] == '//':
            result = operand[operand_index]
            operand_index += 1
            divisor = operand[operand_index]
            operand_index += 1
            for j in range(operator[i+1]):
                result = result // divisor
                if result % divisor == 0:
                    return result
                divisor = operand[operand_index]
            return result
        elif operator[i] == '*':
            result = operand[operand_index]
            operand_index += 1
            for j in range(operator[i+1]):
                result = result * operand[operand_index]
                operand_index += 1
            return result
        elif operator[i] == '-':
            result = operand[operand_index]
            operand_index += 1
            for j in range(operator[i+1]):
                result = result - operand[operand_index]
                operand_index += 1
            return result
        elif operator[i] == '+':
            result = operand[operand_index]
            operand_index += 1
            for j in range(operator[i+1]):
                result = result + operand[operand_index]
                operand_index += 1
            return result
    return 0
