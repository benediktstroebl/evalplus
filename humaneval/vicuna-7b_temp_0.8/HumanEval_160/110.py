
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
    # Check if the operator and operand lists have the correct lengths
    if len(operator) < len(operand)-1:
        raise ValueError("Operator list has less than the required length")
    if len(operand) < 2:
        raise ValueError("Operand list has less than the required length")
    
    # Build the expression
    expression = ""
    for i in range(len(operator)):
        # Perform the basic algebra operation
        operation = operator[i]
        operand_index = i+1
        operand_value = operand[operand_index-1]
        if operation == '+':
            expression += operand_value
        elif operation == '-':
            expression += operand_value*(-1)
        elif operation == '*':
            expression += operand_value
        elif operation == '/':
            if operand_value == 0:
                raise ValueError("Cannot divide by zero")
            expression += operand_value
        elif operation == '**':
            expression += pow(operand_value, operator[i+1])
        else:
            raise ValueError("Invalid operator")
    return expression