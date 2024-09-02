
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
    def do_op(op, num_stack):
        if op == '+':
            return num_stack.pop() + num_stack.pop()
        elif op == '-':
            return num_stack.pop() - num_stack.pop()
        elif op == '*':
            return num_stack.pop() * num_stack.pop()
        elif op == '//':
            return num_stack.pop() // num_stack.pop()
        elif op == '**':
            return num_stack.pop() ** num_stack.pop()
        else:
            return num_stack.pop()
    
    op_stack = list()
    num_stack = list()
    for num in operand:
        if type(num) == int and num >= 0:
            num_stack.append(num)
        elif type(num) == str and num in operator:
            op_stack.append(num)
        elif num in operator:
            result = do_op(op_stack.pop(), num_stack)
            num_stack.append(result)
    result = do_op(op_stack.pop(), num_stack)
    return result

