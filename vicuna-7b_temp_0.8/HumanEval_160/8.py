
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
    # Checking input
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator list and operand list should have the same length.")
    if not any(op in ['+', '-', '*', '/'] for op in operator):
        raise ValueError("Operator list should contain at least one operator.")
    if not all(op[0] >= 0 for op in operator):
        raise ValueError("Operand list should contain only non-negative integers.")

    # Evaluation of the expression
    operand_index = 1
    result = operand[0]
    for i in range(1, len(operand)):
        # Get the operator and its operands
        operator_index = operator[0]
        operand_i = operand[i]
        operand_j = operand[i + 1]

        # Evaluate the expression
        if operator_index == '/':
            if operand_i == 0:
                raise ValueError("Cannot divide by zero.")
            if operand_j in [0, -1]:
                raise ValueError("Cannot use -1 as a divisor.")
            result = result / operand_j
        elif operator_index == '**':
            result = operator_j(result, operand_i)
        elif operator_index == '*':
            result = result * operand_i
        elif operator_index == '-':
            result = result - operand_i
        elif operator_index == '+':
            result = result + operand_i

        # Update the operand index
        operand_index += 1

    return result