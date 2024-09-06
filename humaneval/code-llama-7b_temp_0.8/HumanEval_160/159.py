
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
    op_dict = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '//': lambda x, y: x // y,
        '**': lambda x, y: x ** y,
    }

    stack = []
    for op in operator:
        if op == '(':
            stack.append(int(operand.pop(0)))
        elif op == ')':
            while stack and stack[-1] != '(':
                stack[-2] = op_dict[stack[-2]](stack[-2], stack.pop())
            stack.pop()
        else:
            stack.append(op_dict[op](stack.pop(), int(operand.pop(0))))
    return stack.pop()

