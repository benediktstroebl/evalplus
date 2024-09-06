
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
    # Check if the operator list has at least one operator and operand list has at least two operands
    if len(operator) > 0 and len(operand) >= 2:
        # Concatenate the operator and operand list
        operand = operand + [operator[0]]
        # Use the first operator to apply operations on the operands
        result = operator[0]
        for i in range(1, len(operator)):
            # If the next operator is not a modulus operator (%)
            if operator[i] != '%':
                # If the next operator is an addition (+)
                if operator[i] == '+':
                    # Append the next operand to the result
                    result = result + operand.pop(0)
                # If the next operator is a subtraction (-)
                elif operator[i] == '-':
                    # Append the next operand to the result
                    result = result + operand.pop(0)
                # If the next operator is a multiplication (*)
                elif operator[i] == '*':
                    # Append the next operand to the result
                    result = result + operand.pop(0)
                # If the next operator is a floor division (//)
                elif operator[i] == '/':
                    # Append the next operand to the result
                    result = result + operand.pop(0)
                # If the next operator is an exponentiation (**)
                elif operator[i] == '**':
                    # Append the next operand to the result
                    result = result + operand.pop(0)
            # If the next operator is a modulus operator (%)
            elif operator[i] == '%':
                # Append the next operand to the result
                result = result + operand.pop(0)
            # Otherwise, an error is raised
            else:
                raise ValueError("Invalid operator")
        return result
    # If the operator list is not long enough, an error is raised
    else:
        raise ValueError("Operator list is too short")
