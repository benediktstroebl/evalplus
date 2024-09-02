
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
    
    def do_operation(op1, op2):
        if op1 == '+':
            return op2 + op2
        elif op1 == '-':
            return op2 - op2
        elif op1 == '*':
            return op2 * op2
        elif op1 == '//':
            if op2 <= 0:
                return 0
            return op2 / op2
        elif op1 == '**':
            return op2 ** op2
        else:
            return 0

    print(operator, operand, do_operation(operator[0], operand[0]), do_operation(operator[1], operand[1]), do_operation(operator[2], operand[2]), sep=' ')
    return (do_operation(operator[0], operand[0]), do_operation(operator[1], operand[1]), do_operation(operator[2], operand[2]))
