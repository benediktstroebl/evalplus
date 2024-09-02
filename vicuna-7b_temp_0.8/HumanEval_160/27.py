
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
    # Convert the operator list to a tuple
    operator_tuple = tuple(operator)
    # Check if the operator is a valid operator
    if not (operator_tuple in ALGEBRA_OPERATORS):
        print("Invalid operator")
        return None

    # Check if the operand list has at least two elements
    if len(operand) < 2:
        print("Operand list is empty")
        return None

    # Get the first and second elements from the operand list
    operand1 = operand[0]
    operand2 = operand[1]
    # Get the first and second elements from the operator list
    operator1 = operator[0]
    operator2 = operator[1]

    # Perform the operation using the two elements and the two operators
    if operator1 == ALGEBRA_OPERATORS[operator2]:
        if operand1 == 0:
            return float('inf')
        else:
            return float('-inf')
    else:
        if operator1 == ALGEBRA_OPERATORS[operator2] == ALGEBRA_OPERATORS['//']:
            result = float(operand2)
            return result
        else:
            return float('inf')
