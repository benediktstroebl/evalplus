
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
    operand = [int(operand[i]) for i in range(len(operand)-1)]
    operator_list = [operator[i:i+2] for i in range(0, len(operator), 2)]
    expression = ' '.join([operator[0]] + operator_list + [operand[0]])
    for i in range(1, len(expression)):
        operator_name = expression[i]
        operator = operator_list[i]
        operand_i = operand[i]
        if operator == '*':
            result = eval(expression[:i] + str(operand_i) + expression[i+1:])
            result = round(result)
        elif operator == '/':
            if not operand_i % 1:
                result = eval(expression[:i] + str(operand_i) + expression[i+1:])
                result = round(result)
            else:
                result = 0
        elif operator == '**':
            result = pow(eval(expression[:i] + str(operand_i) + expression[i+1:]), 2)
            result = round(result)
        else:
            result = eval(expression[:i] + str(operand_i) + expression[i+1:])
            result = round(result)
    return result
