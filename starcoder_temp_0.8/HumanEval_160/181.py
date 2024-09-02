
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
    
    op_len = len(operator)
    op_len_minus_1 = op_len - 1
    if op_len_minus_1!= len(operand):
        raise Exception("operator and operand lists are not the same length")
    for i in operator:
        if not i in ['+', '-', '*', '//', '**']:
            raise Exception("operator is not a valid operator")

    def evaluate(i, j, operator):
        if operator[i] == "+":
            return operand[i] + operand[i + 1]
        elif operator[i] == "-":
            return operand[i] - operand[i + 1]
        elif operator[i] == "*":
            return operand[i] * operand[i + 1]
        elif operator[i] == "//":
            return operand[i] // operand[i + 1]
        elif operator[i] == "**":
            return operand[i] ** operand[i + 1]
    
    result = evaluate(0, 1, operator)
    for i in range(op_len_minus_1):
        result = evaluate(i, i + 2, operator)

    return result

