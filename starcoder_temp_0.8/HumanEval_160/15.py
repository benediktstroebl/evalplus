
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
    assert(len(operator) == len(operand) - 1), "Invalid operator and operand."
    for op in operator:
        assert(op in ['+', '-', '*', '//', '**']), "Invalid operator."
    assert(all(op in '+-*/' for op in operator)), "Invalid operator."
    assert(all(op in '+-*/' for op in operator)), "Invalid operator."
    assert(all(isinstance(op, int) for op in operand)), "Invalid operand."
    assert(all(op >= 0 for op in operand)), "Invalid operand."
    assert(len(operator) > 0), "Operator list has no operator."
    assert(len(operand) > 0), "Operand list has no operand."
    
    expression = ''
    for i, op in enumerate(operator):
        if op == '+':
            expression += str(operand[i])
        elif op == '-':
            expression +='-'+ str(operand[i])
        elif op == '*':
            expression +='*'+ str(operand[i])
        elif op == '//':
            expression +='//' + str(operand[i])
        elif op == '**':
            expression +='**'+ str(operand[i])
    expression +='='+ str(operand[-1])

    return eval(expression)
