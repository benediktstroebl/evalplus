
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
    operands = operand.pop(0)
    expression = []
    for i in range(len(operator)):
        operator_value = operator[i]
        operand_value = operands[i-1]
        if operator_value == '+':
            expression.append(operand_value)
        elif operator_value == '-':
            expression.append(operand_value*-1)
        elif operator_value == '*':
            expression.append(operand_value)
        elif operator_value == '**':
            expression.append(int(operand_value)**int(operator[i+1]))
        elif operator_value == '//':
            expression.append(int(operand_value)//int(operator[i+1]))
    expression_val = eval(str(expression))
    return expression_val
