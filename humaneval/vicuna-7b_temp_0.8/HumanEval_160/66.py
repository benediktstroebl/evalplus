
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
    operands = list(range(len(operand)))
    evaluation = 0
    for i, operand_i in enumerate(operand):
        for j, operator_j in enumerate(operator):
            if (i, j) not in [ (k, l) for k, l in enumerate(operand) if l == operand_i ]:
                continue
            if operator_j == '**':
                evaluation += operand_i ** int(operator_j[1:])
            elif operator_j == '//':
                if int(operator_j[1:]) % 2 == 0:
                    evaluation += int(operator_j[1:]) / int(operand_i)
                else:
                    evaluation += int(operator_j[1:]) * int(operand_i)
            else:
                evaluation += operator_j[0] * operand_i
    return evaluation
