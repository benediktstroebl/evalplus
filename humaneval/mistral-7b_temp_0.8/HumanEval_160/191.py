
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
    import operator

    # TODO: Implement the function

    # Create a dictionary of function pointers
    function_dict = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '**': operator.pow,
        '//': operator.floordiv
    }

    # Create a stack to store the operands and operators
    stack = []

    # Iterate over the operator list in reverse order
    for i in range(len(operator)):
        # Check if the current operator is '//'
        if operator[i] == '//':
            # Pop the top two elements from the stack
            divider, dividend = stack.pop(), stack.pop()
            # Calculate the floor division and push the result to the stack
            stack.append(dividend // divider)
        # Check if the current operator is '**'
        elif operator[i] == '**':
            # Pop the top element from the stack
            base = stack.pop()
            # Calculate the power and push the result to the stack
