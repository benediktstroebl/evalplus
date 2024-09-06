
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
    # Get the number of operators
    num_ops = len(operator)

    # Get the number of operands
    num_ops_list = len(operand)
    num_ops = num_ops - 1
    num_ops_list = num_ops_list - 1

    # Initialize the result to the number of operands
    result = operand[0]

    # Evaluate the expression by using the basic operations
    for i in range(num_ops):
        # Get the next operator
        operator_index = i
        operator_str = operator[operator_index][0]

        # Get the next operand
        operand_index = i + 1
        operand_value = operand[operand_index]

        # Evaluate the operator
        if operator_str == '+':
            result = result + operand_value
        elif operator_str == '-':
            result = result - operand_value
        elif operator_str == '*':
            result = result * operand_value
        elif operator_str == '/':
            result = result / operand_value
        elif operator_str == '**':
            result = pow(result, operand_value)

    return result
