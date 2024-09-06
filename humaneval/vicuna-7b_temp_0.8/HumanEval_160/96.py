
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
    expression = ""
    operands = []
    for operator, operand in zip(operator, operand):
        if len(operator) < 2 or len(operand) < 2:
            raise ValueError("The length of operator list is equal to the length of operand list minus one.")
        if operator[0] == '^':
            exponentiation_expression = "**"
        else:
            exponentiation_expression = ""
        for i, operand_ in enumerate(operand):
            if i == 0 or i == 1:
                expression += operator[i]
            else:
                if exponentiation_expression:
                    exponentiation_expression += " " + operator[i]
                else:
                    expression += operator[i]
                operands.append(int(operand_))
                operand_list = [int(x) for x in operand[i+1:] if x.isnumeric()]
                expression += "(" + ",".join(map(str, operand_list)) + ")"
                if operand[i+1] != 0:
                    operands.append(0)
    result = ""
    if operator[0] == '*':
        result = expression
        for i in range(len(expression) - 1, -1, -1):
            operand_list = [int(x) for x in operand[i.split(expression[i])[1]+1:i.split(expression[i])[0]+1] if x.isnumeric()]
            expression = expression.replace("{0}", operand_list[0])
            if expression[-1] == '*':
                expression = expression[:-1]
            result += " " + expression
    elif operator[0] == '/':
        while expression[-1] == '0':
            expression = expression[:-1]
        result = expression[:-1]
    else:
        result = expression
    return result
