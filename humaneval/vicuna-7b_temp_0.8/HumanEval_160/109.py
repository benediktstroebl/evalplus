
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
    # Check if the operator list has at least one operator and the operand list has at least two operands
    if len(operator) >= 1 and len(operand) >= 2:
        # Find the operator and operand of the first operator in the operator list
        operator_index = 0
        operand_index = 0
        for i in range(len(operator)):
            if operator[i] == operator[operator_index]:
                operator_index += 1
            else:
                break
        for i in range(len(operand)):
            if operand[i] == operand[operand_index]:
                operand_index += 1
            else:
                break

        # Check if the operator is a valid operator for the given operand
        if operator[operator_index] in ['+', '-', '*']:
            # If the operator is addition, multiply or subtraction
            if operator[operator_index] == '+':
                result = operand[operand_index]
            elif operator[operator_index] == '-':
                result = operand[operand_index]
            elif operator[operator_index] == '*':
                result = 1
            else:
                result = 0
            for i in range(len(operator)):
                if operator[i] == operator[operator_index]:
                    operator_index += 1
                    result = result * operand[operand_index]
                else:
                    break
        elif operator[operator_index] == '//':
            # If the operator is floor division
            result = operand[operand_index]
            for i in range(len(operator)):
                if operator[i] == operator[operator_index]:
                    operator_index += 1
                else:
                    break
        else:
            # If the operator is exponentiation
            result = operand[operand_index]
            for i in range(len(operator)):
                if operator[i] == operator[operator_index]:
                    operator_index += 1
                else:
                    break
        # If the operator is not a valid operator, return a zero value
        else:
           
