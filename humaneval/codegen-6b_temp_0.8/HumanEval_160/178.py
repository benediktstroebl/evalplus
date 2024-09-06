
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
    def eval_binary(left, right, op):
        def add(a, b):
            return a + b

        def sub(a, b):
            return a - b

        def mul(a, b):
            return a * b

        def div(a, b):
            if b == 0:
                raise ZeroDivisionError('Cannot divide by zero')
            return a / b

        def exp(a, b):
            return a ** b

        return {'+': add(left, right), '-': sub(left, right), '*': mul(left, right),
                '/': div(left, right), '**': exp(left, right)}[op]

    def recur_algebra(operator, operand, accumulator):
        if not operator:
            return accumulator

        acc = eval_binary(*operator[0:2], operator[2])
        operand = recur_algebra(operator[3:], operand, accumulator=acc)
        return eval_binary(left=acc, right=operand, op=operator[2])

    return recur_algebra(operator, operand, accumulator=0)

