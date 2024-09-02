
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
    # The length of operator list is equal to the length of operand list minus one
    assert len(operator) == len(operand) - 1, "Operator list must have at least one operator"
    
    # Get the first operand from the operand list
    operand_index = 0
    operand_value = operand[operand_index]
    operand_index += 1

    # Get the operator from the operator list
    operator_index = operand_index - 1
    operator_value = operator[operator_index]

    # Initialize the result variable
    result = operand_value

    # Evaluate the expression
    for i in range(1, len(operator)):
        # Get the second operand from the operand list
        operator_index = operand_index - len(operator) + i
        operator_value = operator[operator_index]

        # Evaluate the expression
        if operator_value == '+':
            result += operand_value
        elif operator_value == '-':
            result -= operand_value
        elif operator_value == '*':
            result *= operand_value
        elif operator_value == '**':
            result **= operand_value
        elif operator_value == '/':
            result //= operand_value
        elif operator_value == '//':
            result = result / operand_value

    return result