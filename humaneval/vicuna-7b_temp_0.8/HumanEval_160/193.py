
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
    operands = [operand[0]]
    operator_actions = [operator[0]]
    num_ops = len(operand)
    current_op = operator_actions[0]
    for i in range(num_ops):
        if operator[1] == current_op:
            operand_actions = operand[1:]
            for j in range(num_ops):
                if operand_actions[j] > 0:
                    # The first action is not the last action,
                    # and the next action is not a negative number.
                    if current_op == '**':
                        exponent_base = operand_actions[j]
                        exponent_result = eval(str(exponent_base) + str(current_op))
                    else:
                        result = eval(str(current_op) + str(operand_actions[j]))
                    result = do_algebra(current_op, [result])
                    if current_op == '-':
                        result = -result
                else:
                    result = do_algebra(current_op, [])
            current_op = operator_actions[num_ops]
            operand_actions = operand[num_ops+1:]
        else:
            # The first action is not the last action,
            # and the next action is not a negative number.
            if current_op == '**':
                exponent_base = operand_actions[j]
                exponent_result = eval(str(exponent_base) + str(current_op))
            else:
                result = eval(str(current_op) + str(operand_actions[j]))
            result = do_algebra(current_op, [result])
            if current_op == '-':
                result = -result
            current_op = operator_actions[i+1]
            operand_actions = operand[i+2:]
    return result