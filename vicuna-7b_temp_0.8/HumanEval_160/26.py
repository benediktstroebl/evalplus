
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
    if len(operator) < 1:
        return 0
    elif len(operator) == 1:
        if operator[0] == '0':
            return 0
        else:
            return operator[0]
    else:
        operator_list = list(operator)
        operand_list = [operand[0]]
        for i in range(1, len(operand)):
            operand_list.append(operand[i])
        if operator_list[0] == '1':
            result = 1
        else:
            result = 0
        operator_list.pop(0)
        for i in range(len(operator_list)):
            operator = operator_list[i]
            operand = operand_list[i]
            if operator == '+':
                result = result + operand
            elif operator == '-':
                result = result - operand
            elif operator == '*':
                result = result * operand
            elif operator == '/':
                if operand != 0:
                    result = result / operand
                else:
                    return 0
            elif operator == '**':
                if operand != 0:
                    result = result ** operand
                else:
                    return 0
        return result