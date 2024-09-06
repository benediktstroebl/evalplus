
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
    if len(operator) == len(operand) - 1:
        # Check if the operator is the next operator in the list
        for i in range(len(operator)):
            if operator[i] != operator[i + 1]:
                # Add a 0 to the end of the operator list
                operator += [0] * (len(operator) - i - 1)
                break
        # Use the operator to evaluate the expression
        expr = []
        for i in range(len(operator)):
            expr.append(operator[i])
        expr = ''.join(expr)
        if len(expr) == 0:
            return 1
        if expr[0] == '0':
            return 0
        # Use the operand to evaluate the expression
        operand_expr = 1
        for i in operand:
            operand_expr *= i
        return operand_expr
    else:
        return 0
