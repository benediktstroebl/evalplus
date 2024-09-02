
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

    # Define the order of operations
    ops_order = {'*': 1, '/': 1, '+': 2, '-': 2}
    # Create a new list of operator and operand
    # to be able to manipulate them
    # operator = ['*', '+', '+', '*', '/', '-', '*', '+', '*']
    # operand = [1, 1, 2, 3, 2, 2, 1, 3, 2]
    ops_and_nums = [operator, operand]
    # Join the two list into one
    ops_and_nums = [item for sublist in ops_and_nums for item in sublist]
    # print(ops_and_nums)

    # Iterate over the list and if the element is a operator
    # check if it should be performed first or second.
    # If first, pop the last two elements from the list and
    # peform the operation on them, then insert the result back
    # to the list, and repeat the iteration process.
    # If the operator should be performed second, continue
    # with the next iteration.
    while '+' in ops_and_nums or '-' in ops_and_nums:
        if ops_and_nums[0] == '+' or ops_and_nums[0] == '-':
            # print(ops_and_nums)
            op1 = ops_and_nums.pop(1)
            op2 = ops_and_nums.pop(1)
            if ops_and_nums[0] == '+':
                result = op1 + op2
            else:
                result = op1 - op2
            # print(result)
            ops_and_nums.insert(1, result)
        else:
            ops_and_nums.pop(0)

    while '*' in ops_and_nums or '/' in ops_and_nums:
        if ops_and_nums[0] == '*' or ops_and_num
