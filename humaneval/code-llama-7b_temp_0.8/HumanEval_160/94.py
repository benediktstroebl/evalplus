
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
    if len(operator) == 0 or len(operand) == 1:
        return operand
    if len(operator) != len(operand)-1:
        return -1
    
    operator_list = list(operator)
    operand_list = list(operand)
    
    for index in range(len(operator)):
        eval_str = "{} {} {}".format(operand_list[index], operator_list[index], operand_list[index+1])
        operand_list[index] = eval(eval_str)
        operator_list.pop(0)
    return operand_list[0]

