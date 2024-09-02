
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
    operator_list = operator[:-1]
    operand_list = operand[:-1]
    operator_length = len(operator_list)
    operand_length = len(operand_list)
    if operator_length == 0:
        return 0
    if operand_length == 0:
        return 0
    if operator_length == 1:
        if operator_list[0] == '**':
            return eval_exponentiation(operator_list[1:], operand_list)
        else:
            return eval_arithmetic(operator_list, operand_list)
    result = 0
    for i in range(operator_length):
        operator_index = i
        operand_index = i
        while operator_index < operator_length and operand_index < operand_length:
            if operator_list[operator_index] == '+':
                result = result + operand_list[operand_index]
                operator_index += 1
                operand_index += 1
            elif operator_list[operator_index] == '-':
                result = result - operand_list[operand_index]
                operator_index += 1
                operand_index += 1
            elif operator_list[operator_index] == '*':
                result = result * operand_list[operand_index]
                operator_index += 1
                operand_index += 1
            elif operator_list[operator_index] == '/':
                if operand_list[operand_index] != 0:
                    result = result / operand_list[operand_index]
                    operator_index += 1
                    operand_index += 1
                else:
                    result = "0/undefined"
            elif operator_list[operator_index] == '**':
                result = eval_exponentiation(operator_list[operator_index+1:], operand_list)
                operator_index += 1
                break
            else:
                result = eval_arithmetic(operator_list[operator_index], operand_list[operand_index])
                operator_index += 
