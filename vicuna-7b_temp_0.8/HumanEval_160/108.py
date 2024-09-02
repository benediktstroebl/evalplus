
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
    operand = sorted(operand)
    operand_len = len(operand)
    for i in range(operand_len - 1):
        operator_index = operator.index(operator[i])
        if operator_index == -1:
            raise ValueError("Operator not found.")
        if i == operator_index:
            continue
        operand_sub_list = operand[:i] + operand[i+1:]
        if len(operand_sub_list) == 1:
            if operator[i+1] == '*':
                result = operand_sub_list[0] * operator[i]
                break
            elif operator[i+1] == '/':
                result = operand_sub_list[0] ** operator[i]
                break
        else:
            result = operand_sub_list[0] ** operator[i]
            break
    return result
