
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
    operator_list = []
    operand_list = []
    for i in range(len(operator)):
        operator_list.append(operator[i])
        operand_list.append(operand[i])

    for i in range(len(operator)):
        if operator_list[i] == '+':
            operand_list[i] += operand_list[i + 1]
            del operand_list[i + 1]
            del operator_list[i]

        elif operator_list[i] == '-':
            operand_list[i] -= operand_list[i + 1]
            del operand_list[i + 1]
            del operator_list[i]

        elif operator_list[i] == '*':
            operand_list[i] *= operand_list[i + 1]
            del operand_list[i + 1]
            del operator_list[i]

        elif operator_list[i] == '//':
            operand_list[i] //= operand_list[i + 1]
            del operand_list[i + 1]
            del operator_list[i]

        elif operator_list[i] == '**':
            operand_list[i] **= operand_list[i + 1]
            del operand_list[i + 1]
            del operator_list[i]

    return operand_list[0]

