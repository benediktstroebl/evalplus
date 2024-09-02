
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
    operands = operand[:-1]
    operator_op = operator[-1]

    if not all(op[1] >= 0 for op in operator):
        return 0

    for i, op in enumerate(operator):
        if operator[i][0] == operator_op:
            # handle the operator
            if operator[i][1] == '*':
                product = 1
                for j in range(i, len(operands)):
                    product *= operands[j]
                    if operator[j][1] == operator[i][1]:
                        product %= operands[j]
                result = eval_expression(operand, product)
                break
            elif operator[i][1] == '**':
                result = pow(eval_expression(operand, int(operator[i][2])), operands[i])
                break
            else:
                result = eval_expression(operand, int(operator[i][0]))
                break
        else:
            # handle the operand
            if operand[i] == operand[-1]:
                result = eval_expression(operand[:-1], operand[-1])
                break
            else:
                result = 0
                break
    else:
        return 0
