
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
    if operator == []:
        return operand

    operator.reverse()
    operand.reverse()
    operand_copy = operand[:]
    operand_copy.pop()

    for op in operator:
        while op in operand_copy:
            operand_copy[operand_copy.index(op)] = eval(f'{operand_copy[operand_copy.index(op) - 1]}{op}{operand_copy[operand_copy.index(op) + 1]}')
            operand_copy.pop(operand_copy.index(op) + 1)
            operand_copy.pop(operand_copy.index(op) - 1)
            if operand_copy.index(op) >= len(operand_copy):
                break
    return operand_copy[0]


