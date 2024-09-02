
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
    
    def trim(lst):
        lst = lst[:]
        while lst[0] == 0:
            lst.remove(0)
        while lst[len(lst) - 1] == 0:
            lst.remove(0)
        return lst

    def evaluate_expr(operator, operand):
        if len(operator) == 0:
            return operand[0]
        operator = operator[:]
        operator.reverse()
        if operator[0] == '+':
            return evaluate_expr(operator[1:], [operand[0] + operand[1]])
        if operator[0] == '-':
            return evaluate_expr(operator[1:], [operand[0] - operand[1]])
        if operator[0] == '*':
            return evaluate_expr(operator[1:], [operand[0] * operand[1]])
        if operator[0] == '//':
            return evaluate_expr(operator[1:], [operand[0] // operand[1]])
        if operator[0] == '**':
            return evaluate_expr(operator[1:], [operand[0] ** operand[1]])
    
    def evaluate_func_expr(operator, operand):
        if len(operator) == 0:
            return operand[0]
        operator = operator[:]
        operator.reverse()
        if operator[0] == '+':
            return evaluate_func_expr(operator[1:], [operand[0] + operand[1]])
        if operator[0] == '-':
            return evaluate_func_expr(operator[1:], [operand[0] - operand[1]])
        if operator[0] == '*':
            return evaluate_func_expr(operator[1:], [operand[0] * operand[1]])
        if operator[0] == '//':
            return evaluate_func_expr(operator[1:], [operand[0] // operand[1]])
        if operator[0] == '**':
            return evaluate_func_expr(operator