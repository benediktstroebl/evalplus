
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
    operator_stack = []
    operand_stack = []
    for item in operator:
        if item == '(':
            operator_stack.append(item)
        elif item == ')':
            while operator_stack[-1]!= '(':
                operand_stack.append(operator_stack.pop())
            operator_stack.pop()
        else:
            while operator_stack and operand_stack and operator_stack[-1]!= '(' and \
                    operand_stack[-1] >= operator[item]:
                operator_stack.pop()
                operand_stack.pop()
            operator_stack.append(item)
    while operator_stack:
        operand_stack.append(operator_stack.pop())
    return operand_stack[
