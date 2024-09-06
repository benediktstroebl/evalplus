
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
    if len(operator) <= 1:
        raise ValueError("operator list must have at least one operation, and operand list must have at least two operands")

    eval_list = []
    for i, operator_i in enumerate(operator):
        if i == 0:
            eval_list.append(operator_i)
            eval_list.append(operand[i])
        else:
            if operator_i == '+':
                operand_i = operand[i]
                eval_list.append(operand_i)
                eval_list.append(operator_i)
                eval_list.append(eval_list[-1] + eval_list[-2])
            elif operator_i == '-':
                operand_i = operand[i]
                eval_list.append(operand_i)
                eval_list.append(operator_i)
                eval_list.append(eval_list[-1] - eval_list[-2])
            elif operator_i == '*':
                operand_i = operand[i]
                eval_list.append(operand_i)
                eval_list.append(operator_i)
                eval_list.append(eval_list[-1] * eval_list[-2])
            elif operator_i == '/':
                operand_i = operand[i]
                eval_list.append(operand_i)
                eval_list.append(operator_i)
                eval_list.append(eval_list[-1] // eval_list[-2])
            elif operator_i == '**':
                operand_i = operand[i]
                eval_list.append(operand_i)
                eval_list.append(operator_i)
                eval_list.append(eval_list[-1] ** eval_list[-2])
            else:
                raise ValueError("operator must be one of [+, -, *, /, **]")

    if eval_list[-1] == eval_list[-2]:
        return eval_list[-1]
    else:
        return eval_list[-