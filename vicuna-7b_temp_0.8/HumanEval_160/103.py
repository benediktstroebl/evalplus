
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
    operand = list(operand)
    operator = list(operator)
    if len(operator) != len(operand) - 1:
        raise ValueError("Length of operator list is not equal to the length of operand list - 1")
    operand.append(0)
    operand = [i if i >= 0 else 0 for i in operand]
    operand_evaluated = []
    operator_position = 0
    for i in range(len(operator)):
        if operator[operator_position] == '**':
            operator_position += 1
            while operator[operator_position] == '*':
                operator_position += 1
            power, operand_index = map(int, operator[operator_position:].split())
            operand[operand_index] = (operand[operand_index] ** power) if power >= 0 else 1
            operator_position += 1
        elif operator[operator_position] == '*':
            operator_position += 1
            operand_evaluated.append(operand[operator_position - 1] * operand[operator_position])
        elif operator[operator_position] == '-':
            operator_position += 1
            operand_evaluated.append(operand[operator_position - 1] - operand[operator_position])
        elif operator[operator_position] == '+':
            operator_position += 1
            operand_evaluated.append(operand[operator_position - 1] + operand[operator_position])
        elif operator[operator_position] == '-':
            operator_position += 1
            operand_evaluated.append(operand[operator_position - 1] - operand[operator_position])
        elif operator[operator_position] == '=':
            operator_position += 1
            operand_index = int(operator[operator_position])
            operand[operand_index] = operand_evaluated.pop()
    return operand_evaluated[::-1]
