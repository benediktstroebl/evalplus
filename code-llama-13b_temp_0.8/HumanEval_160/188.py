
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
    def do_eval(operand_list, operator_list):
        if not operator_list:
            return operand_list[0]
        ops = {'+': lambda a, b: a + b,
               '-': lambda a, b: a - b,
               '*': lambda a, b: a * b,
               '//': lambda a, b: a // b,
               '**': lambda a, b: a ** b
              }
        op1 = operand_list[0]
        op2 = operand_list[1]
        op_symb = operator_list[0]
        return do_eval([ops[op_symb](op1, op2)] + operand_list[2:], operator_list[1:])

    return do_eval(operand, operator)

