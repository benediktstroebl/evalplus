
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
    # Check if the given operator list is valid
    if len(operator) != len(operand) - 1:
        raise ValueError("Operator list is not valid")
    # Check if the given operand list is valid
    if not isinstance(operand, list) or not all(isinstance(item, int) for item in operand):
        raise ValueError("Operand list is not valid")

    # Evaluate the expression
    operands = operand.pop(0)
    expression = []
    for i, operator in enumerate(operator):
        if isinstance(operator, str):
            operator = operator.upper()
            if operator == '*':
                expression.append(eval_mul(operands, operand[i+1]))
            elif operator == '/':
                expression.append(eval_div(operands, operand[i+1]))
            elif operator == '+':
                expression.append(eval_add(operands, operand[i+1]))
            elif operator == '-':
                expression.append(eval_sub(operands, operand[i+1]))
            else:
                raise ValueError("Invalid operator")
        else:
            raise ValueError("Operator should be a string")
    return eval_expr(expression)
