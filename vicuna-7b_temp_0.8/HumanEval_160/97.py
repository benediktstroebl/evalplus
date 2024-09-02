
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
    operand = [i for i in operand if i >= 0]
    if len(operator) != len(operand)-1:
        raise ValueError("Operator list must have at least one operator and operand list must have at least two operands")
    for i in range(len(operator)):
        operator_index = operator.index(operator[i])
        operand_index = operator.index(operator[i+1])
        if operator[i] == '*':
            result = eval_mul(operand[operand_index], operand[operand_index-1])
        elif operator[i] == '/':
            result = eval_div(operand[operand_index], operand[operand_index-1])
        elif operator[i] == '**':
            result = pow(eval_mul(operand[operand_index], operand[operand_index-1]), operand[operand_index-2])
        else:
            raise ValueError("Invalid operator")
    return result

