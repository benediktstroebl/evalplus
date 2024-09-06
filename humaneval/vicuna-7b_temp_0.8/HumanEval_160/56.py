
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
    operator_len = len(operator_list)
    operand_len = len(operand_list)
    result = operand_list[0]
    for i in range(1, operand_len):
        for j in range(0, operator_len):
            operator_index = j + 1
            operand_index = i + 1
            if operator_index >= operand_len:
                break
            if operator_list[operator_index] == '**':
                if operator_index - 1 >= operand_len:
                    result = operator_list[operator_index - 1] ** result
                else:
                    result = result ** operator_list[operator_index - 1]
            elif operator_list[operator_index] == '//':
                if operator_index - 1 >= operand_len:
                    result = (result / operand_list[operator_index - 1]) ** operator_list[operator_index + 1]
                else:
                    result = (result / operand_list[operator_index - 1]) ** operator_list[operator_index + 1] ** -1
            elif operator_list[operator_index] == '+':
                if operator_index - 1 >= operand_len:
                    result = result + operand_list[operator_index - 1]
                else:
                    result = result + (operator_list[operator_index - 1] * operand_list[operator_index - 1]) ** -1
            elif operator_list[operator_index] == '-':
                if operator_index - 1 >= operand_len:
                    result = result - operand_list[operator_index - 1]
                else:
                    result = result - (operator_list[operator_index - 1] * operand_list[operator_index - 1]) ** -1
            elif operator_list[operator_index] == '*':
                if operator_index - 1 >= operand_len:
                    result = result * operand_list[operator
