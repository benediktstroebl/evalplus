
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
    operator_list = operator[:-1]
    operand_list = operand[:-1]
    expression = ""
    for i in range(len(operator_list)):
        left_op = operator_list[i]
        left_val = operand_list[i]
        right_op = operator_list[i+1] if i+1 < len(operator_list) else None
        right_val = operand_list[i+1] if i+1 < len(operand_list) else None

        # perform the basic algebra operation
        if left_op == '+':
            expression += str(left_val)
        elif left_op == '-':
            expression += str(left_val)
        elif left_op == '*':
            expression += str(left_val)
        elif left_op == '/':
            if not right_op:
                raise ValueError("division by zero")
            expression += str(left_val)
            expression += str(right_val)
            expression += str(operator_list[i+2])
        elif left_op == '**':
            if not right_op:
                raise ValueError("non-integer exponent")
            expression += str(left_val)
            expression += str(right_val)
            expression += str(operator_list[i+1])

    return eval_expression(expression)
