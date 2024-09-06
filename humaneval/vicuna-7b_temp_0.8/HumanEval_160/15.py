
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
    op_list = operator.split(', ')
    operand_list = operand.split(', ')

    # Check if the number of operations is equal to the number of operands
    if len(op_list) != len(operand_list):
        raise ValueError("The number of operations should be equal to the number of operands.")

    # Extract the operations from the operator list
    operations = [op_list[i:i+2] for i in range(0, len(op_list), 2)]

    # Create a dictionary to keep track of the operands and their values
    operand_dict = {}

    for i, operand_tuple in enumerate(operand_list):
        operand = operand_tuple[0]
        value = operand_tuple[1]
        operand_dict[operand] = value

    # Perform the operations on the operands
    result = []
    for op, operand in zip(operations, operand_list):
        operand = operand_dict.get(operand, 0)
        result.append(getattr(operand, op))

    return eval_list(result)
