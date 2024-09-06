
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
    eval_list = []
    for i in range(len(operator)):
        operator_list = operator[:i+1]
        if len(operator_list) >= 1:
            operand_list = operand[:i+1]
            if len(operand_list) > 1:
                op = operator[i]
                eval = 0
                for j in range(len(op)):
                    eval = eval * operand_list[j] if j < len(operand_list) else eval
                eval_list.append(eval)
    return eval_list[0]