
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
    # build the list of operands, and the list of operators to use
    operand_list = [i for i in operand]
    operator_list = [i for i in operator]
    operand_list = [int(i) for i in operand_list]
    # now we need to work out the expression
    # for example: 2 + 3 * 4 - 5
    # need to work out 3 * 4 - 5 first
    # this will be done with a while loop, which will loop until there are no more operators in the operator_list
    # if there are no more operators left in the operator_list, then we are done, and can calculate the expression
    # so we first check that the length of operator list is equal to the length of operand list minus one, as explained above
    while len(operator_list) < (len(operand_list) - 1):
        # need to pop a left_operand and a right_operand from the operand_list
        # left_operand is the first element in the list
        left_operand = operand_list[0]
        # right operand is the last element in the list
        right_operand = operand_list[-1]
        # now to check if we can perform the operation on the two operands
        # check if the current operator is +
        if operator_list[0] == '+':
            # if it is +, then just add the operands together
            result = left_operand + right_operand
        # check if the current operator is -
        elif operator_list[0] == '-':
            # if it is -, then subtract the right_operand from the left_operand
            result = left_operand - right_operand
        # check if the current operator is *
        elif operator_list[0] == '*':
            # if it is *, then multiply the operands
            result = left_operand * right_operand
        # check if the current operator is //
        elif operator_list[0] == '//':
            # if it is //, then divide the left_operand by the right_operand
            result = left_operand // right_operand
        # check if the current operator is **
        elif operator_list[0] == '**':
            # if it is **, then exponentiate the left_operand by the right_operand
            result = left_operand ** right_operand
        # now the result is the result of the operation
