
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
    # Get the operators of the operator list
    operator_list = [operator[i][0] for i in range(len(operator)-1)]
    # Get the operands of the operator list
    operand_list = [operand[i] for i in range(len(operand)-1)]
    # Evaluate the expression by using the operands and operators
    result = eval_expr(*[operand_list[i] + operator_list[j] for j in range(len(operator_list))])
    # Print the result
    print(result)
