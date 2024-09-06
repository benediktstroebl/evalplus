
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
    def reduce_operator(arr, op, arr_type):
        """
        Reduce operator.
        arr: a list of operands.
        op: a operator from operator list.
        arr_type: a type of arr.
        """
        if op == '+':
            return sum(arr)
        elif op == '*':
            return reduce(operator.__mul__, arr, 1)
        elif op == '-':
            return reduce(operator.__sub__, arr, 0)
        elif op == '//':
            return reduce(operator.__floordiv__, arr, 0)
        else:
            return reduce(operator.__pow__, arr, 1)

    result = reduce(operator.__add__, operator, 0)
    if len(operator) > 1:
        for i in range(len(operator)):
            if i % 2 == 0:
                result = reduce_operator(operand[i], operator[i], 'int')
            elif i % 2 == 1:
                result = reduce_operator(operand[i], operator[i
