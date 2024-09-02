
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

    # operator_index = 0
    # start_index = 0
    # end_index = 0
    # num_of_operands = len(operand)

    # while operator_index < num_of_operands:
    #     end_index = end_index + 1

    #     if operator_index < num_of_operands - 1:
    #         if operator[operator_index] == '+' or operator[operator_index] == '-':
    #             continue
    #         elif operator[operator_index] == '*':
    #             operand[start_index] = operand[start_index] * operand[end_index]
    #             operand.pop(end_index)
    #             operand.pop(start_index)
    #             operator.pop(operator_index)
    #             end_index = start_index
    #             operator_index = operator_index - 2
    #             continue
    #         else:
    #             operand[start_index] = operand[start_index] // operand[end_index]
    #             operand.pop(end_index)
    #             operand.pop(start_index)
    #             operator.pop(operator_index)
    #             end_index = start_index
    #             operator_index = operator_index - 2
    #             continue
    #     else:
    #         if operator[operator_index] == '+' or operator[operator_index] == '-':
    #             operand[start_index] = operand[start_index] + operand[end_index]
    #             operand.pop(end_index)
    #             operand.pop(start_index)
    #             operator.pop(operator_index)
    #             end_index = start_index
    #             operator_index = operator_index - 2
    #             continue
    #         elif operator[operator_index] == '*':
    #             operand[start_index] = operand[start_index] * operand[end_index]
    #             operand.pop(end_index)
