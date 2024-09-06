
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

    if not operator or len(operator) + 1!= len(operand) or not all(x in OPERATIONS for x in operator):
        raise Exception("Invalid input")

    stack = []
    for i in range(len(operator)):
        o = operator[i]
        a = operand[i]
        b = operand[i+1]
        if o == "+":
            stack.append(a+b)
        elif o == "-":
            stack.append(a-b)
        elif o == "*":
            stack.append(a*b)
        elif o == "//":
            stack.append(a//b)
        elif o == "**":
            stack.append(a**b)

    return stack.pop()
