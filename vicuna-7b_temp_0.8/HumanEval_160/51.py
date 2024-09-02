
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
    operand_index = len(operand) - 1
    operator_index = [i for i, op in enumerate(operator) if op[0] == operator[i]][0]
    operand_list = [operand[i] for i in operand_index]
    result = 0
    for op in operator:
        if op[0] == operator[operator_index]:
            if op[1] == '+':
                result = result + operand_list[0]
            elif op[1] == '-':
                result = result - operand_list[0]
            elif op[1] == '*':
                result = result * operand_list[0]
            elif op[1] == '/':
                result = result / operand_list[0]
            elif op[1] == '**':
                result = pow(result, operand_list[0])
            else:
                print("error: unknown operator")
                return None
    return result