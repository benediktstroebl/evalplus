
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
    # write your answer between #start and #end
    #start
    oper = {'+': operator[0],'*':operator[1],'-':operator[2]}
    nums = operand
    ops = {'+': 0, '*': 1, '-': 2}
    stack = []
    if len(nums) == 0:
        return 'please input an integer'
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return nums[0] + nums[1]
    for i in range(len(nums)):
        if i == 0:
            stack.append(nums[0])
            continue
        if i == 1:
            if nums[1] == 0:
                return 'please input a non-zero integer'
            if oper['+'] == '*':
                stack.append(nums[0] * nums[1])
                continue
            elif oper['+'] == '-':
                stack.append(nums[0] - nums[1])
                continue
        if i == 2:
            if nums[2] == 0:
                return 'please input a non-zero integer'
            if oper['-'] == '-':
                stack.append(nums[0] - nums[1] - nums[2])
                continue
            elif oper['-'] == '*':
                stack.append(nums[0] * nums[1] - nums[2])
                continue
        if i == 3:
            if oper['*'] == '*':
                stack.append(stack[-1] * nums[3])
                continue
            elif oper['*'] == '/':
                stack.append(stack[-1] // nums[3])
                continue
            elif oper['-'] == '/':
                stack.append(stack[-1] // nums[3] - nums[2])
                continue
            else:
                stack.append(stack[-1] - nums[2] + nums[3])
                continue
        if i == 4:
            if oper['/'] == '/':
                stack.append(stack[-1] // nums[4])
                continue
            elif oper['*'] == '**':
                stack.append(stack[-1] ** nums[4])
                continue
            elif oper['*'] == '*':
                stack.append(stack[-1] * nums[4])
                continue
            elif oper['*']
