
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
    operand_list = operand[:-1]
    operator_list = operator[:-1]
    evaluator = []
    for i in range(len(operand_list)):
        evaluator.append(0)
    for i in range(len(operator_list)):
        operation = operator_list[i][0]
        operand_i = operand_list[i]
        if operation == '+':
            evaluator[-1] += operand_i
        elif operation == '-':
            evaluator[-1] -= operand_i
        elif operation == '*':
            evaluator[-1] *= operand_i
        elif operation == '//':
            if operand_i % 1 not in (0, 1):
                raise ValueError("Invalid operand for division")
            evaluator[-1] //= operand_i
        elif operation == '**':
            evaluator[-1] **= operand_i
        else:
            raise ValueError("Invalid operation")
    return evaluator[-1]
