
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
    operand_list = operand[:-1]
    operator_list = operator[:-1]
    operator_list = [x[0] for x in operator_list]
    # Find the number of operands in the operator list
    num_ops = len(operator_list)
    # Use the operator list to get the list of operators
    operators = [x[1] for x in operator_list]
    # Use the operand list to get the list of operands
    operands = [x[2] for x in operand_list]
    # Use the operators and operands to build the algebraic expression
    expression = []
    for i in range(num_ops - 1):
        operator = operators[i]
        operand = operands[i]
        expression.append(operator)
        expression.append(operand)
        # Add a 0 at the end to make the expression true
        expression.append(0)
    # Evaluate the algebraic expression
    result = eval(str(expression))
    return result
