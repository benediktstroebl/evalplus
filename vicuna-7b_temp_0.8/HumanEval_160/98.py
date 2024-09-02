
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
    operand_len = len(operand)
    if operand_len < 2:
        return 0

    for i in range(operand_len):
        if i == 0:
            continue

        operator_idx = int(operator[i])
        op = operator[i+1]
        operand_val = operand[i]

        if op == '+':
            result = result + operand_val
        elif op == '-':
            result = result - operand_val
        elif op == '*':
            result = result * operand_val
        elif op == '/':
            if not is_valid_division(operand_val, operand[i+2]):
                return 0
            result = result / operand_val
        elif op == '**':
            if not is_valid_exponentiation(operand_val, operand[i+1]):
                return 0
            result = result ** operand_val
        else:
            return 0

    return result