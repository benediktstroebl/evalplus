
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
    if len(operator) == len(operand) - 1:
        operator_index = 0
    else:
        raise ValueError("Operator list is not valid")
    operand_index = 0
    operand_values = [int(value) for value in operand]
    result = operand_values[operand_index]
    if operator_index < len(operator):
        operator_operand = operator[operator_index]
        if operator_operand == '*':
            for i in range(operand_index + 1, len(operand_values)):
                result *= operand_values[i]
        elif operator_operand == '/':
            for i in range(operand_index + 1, len(operand_values)):
                if operand_values[i] == 0:
                    raise ValueError("Cannot divide by zero")
                result /= operand_values[i]
        elif operator_operand == '**':
            for i in range(operand_index + 1, len(operand_values)):
                result **= operand_values[i]
        else:
            raise ValueError("Invalid operator")
        result = result * result
    return result