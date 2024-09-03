def do_algebra(operator, operand):
    """
    Given two lists operator, and operand.
        - The length of operator list is equal to the length of operand list minus one
        - operator list has at least one operator, and operand list has at least two operands
        - the list of non-negative integers is used
    """
    # Ensure the length of both lists is the same minus one
    assert len(operator) == len(operand) - 1
    operator = list(operator) + [None] * (len(operand) - 1)
    operand = list(operand)
    # Define the basic algebra operations
    op_list = ['+', '*', '-']
    for i, o in enumerate(operator):
        operand[i + 1] = eval(o) + evaluate(operand[:i + 1], op_list[:i + 1])
    return evaluate(operand, op_list)
def evaluate(operand, op_list):
    """
    Built the expression and returns the evaluation
    """
    result = 0
    for o in op_list:
        result += eval(o) * operand
    return result