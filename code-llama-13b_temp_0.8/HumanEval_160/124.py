
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
    if len(operator) != len(operand) - 1:
        raise ValueError(
            "The length of operator list must be equal to the length of operand list minus one.")
    if len(operand) < 2:
        raise ValueError(
            "The length of operand list must be greater than two")
    if any(i < 0 for i in operand):
        raise ValueError("The operand list must be a list of non-negative integers")
    if not all(i in ['+', '-', '*', '//', '**'] for i in operator):
        raise ValueError(
            "The operator list must be a list of the basic algebra operations")
    # use two stacks to save the operators and operands respectively
    op_stk = []
    num_stk = []
    for i in range(len(operator)):
        op_stk.append(operator[i])
        num_stk.append(operand[i])
        num_stk.append(operand[i+1])
    # first pop out the number, then perform the operation
    result = num_stk.pop()
    while op_stk:
        op = op_stk.pop()
        if op == '+':
            result += num_stk.pop()
        elif op == '-':
            result -= num_stk.pop()
        elif op == '*':
            result *= num_stk.pop()
        elif op == '//':
            result //= num_stk.pop()
        elif op == '**':
            result **= num_stk.pop()
    return result

