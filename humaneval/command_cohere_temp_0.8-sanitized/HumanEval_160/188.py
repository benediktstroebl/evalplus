def do_algebra(operator, operand):
    # type: (List[str], List[int]) -> int
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
    # Check for empty operand or empty or invalid operator
    if not operand or not operator or len(operator) != len(operand) - 1:
        raise ValueError("Operand and operator lists must not be empty, and the length of the operator list must be equal to the length of the operand list minus one.")

    # Reverse the operand list to match operator list order
    operand = operand[::-1]
    result = 0
    curr_op = operator.pop()
    for op in operand:
        if curr_op == '*':
            result *= op
        elif curr_op == '//':
            result //= op
        elif curr_op == '+':
            result += op
        elif curr_op == '-':
            result -= op
        elif curr_op == '**':
            result **= op
        else:
            raise ValueError(f"Invalid operator: {curr_op}")
        curr_op = operator.pop()
    return result