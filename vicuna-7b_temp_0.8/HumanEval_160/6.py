
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
    # Get the number of operations in the operator list
    num_ops = len(operator)

    # Get the number of operands in the operand list
    num_ops_without_1 = len(operand) - 1

    # Get the operator from the operator list
    operator_val = operator[0]

    # Get the operand from the operand list
    operand_val = operand[1]

    # Calculate the result
    result = operand_val

    # Iterate through the operator list
    for i in range(num_ops):
        # Get the operands from the operand list
        operand_val = operand[i + 1]

        # Get the operator
        operator_val = operator[i]

        # Perform the operation
        if operator_val == '+':
            result += operand_val
        elif operator_val == '-':
            result -= operand_val
        elif operator_val == '*':
            result *= operand_val
        elif operator_val == '/':
            result /= operand_val
        elif operator_val == '**':
            result **= operand_val
        else:
            print("Operator not recognized")

    return result
