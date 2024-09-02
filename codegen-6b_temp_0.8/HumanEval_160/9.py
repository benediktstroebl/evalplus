
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
    # don't change this code
    def add(N1, N2):
        return N1 + N2

    def sub(N1, N2):
        return N1 - N2

    def mul(N1, N2):
        return N1 * N2

    def div(N1, N2):
        return N1 // N2

    def pow(N1, N2):
        return N1 ** N2

    def eval(operator, operand, l):
        while len(l) != 1:
            if operator[0] == '+':
                l = add(l[0], l[1])
            elif operator[0] == '-':
                l = sub(l[0], l[1])
            elif operator[0] == '*':
                l = mul(l[0], l[1])
            elif operator[0] == '/':
                l = div(l[0], l[1])
            elif operator[0] == '**':
                l = pow(l[0], l[1])
        return l[0]

    return eval(operator, operand, [0])

