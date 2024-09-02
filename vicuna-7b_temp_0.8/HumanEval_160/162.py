
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
    expression = operator
    operand_list = operand
    operand_list = [int(val) for val in operand_list]
    for i in range(len(expression)):
        if expression[i] == '*':
            for j in range(i, len(expression)):
                expression[j] = expression[j] * operand_list[i]
                operand_list = operand_list[i+1:]
        elif expression[i] == '/':
            for j in range(i+1, len(expression)):
                expression[j] = expression[j] / operand_list[i]
                operand_list = operand_list[1:]
        elif expression[i] == '^':
            for j in range(i+1, len(expression)):
                expression[j] = expression[j] ** operand_list[i]
                operand_list = operand_list[1:]
        elif expression[i] == '+':
            expression[i] = eval_add(expression[i+1:], operand_list[1:])
        elif expression[i] == '-':
            expression[i] = eval_sub(expression[i+1:], operand_list[1:])
        else:
            raise ValueError("Invalid operator")
    return eval(expression, {'**': operator['**'], '*': operator['*'], '/': operator['/'], '+': operator['+'], '-': operator['-']})
