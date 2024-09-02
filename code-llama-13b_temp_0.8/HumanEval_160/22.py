
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
    # get the first element of the operand as the first term in our expression.
    term = operand[0]
    # for each operation, do the operation on the term and the next element in the operand list.
    # do this for every operation.
    # once all operations are done, we are left with one term, which is our result.
    for i, op in enumerate(operator):
        term = eval(f"{term} {op} {operand[i+1]}")
    return term
