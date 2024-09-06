
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
    operand = [x for x in operand if x >= 0]
    if len(operator) == len(operand) - 1:
        # handle the special case when operator is a single element list
        if len(operand) == 2:
            return operator[0]
        else:
            return operator[0] * operand[0]
    else:
        # handle the general case
        operator_idx = 0
        operand_idx = 0
        result = operator[operator_idx]
        while operator_idx < len(operator) and operand_idx < len(operand):
            if operator[operator_idx] == '-':
                result = result * operand[operand_idx]
                operand_idx += 1
            elif operator[operator_idx] == '*':
                result = result * operand[operand_idx]
                operand_idx += 1
            elif operator[operator_idx] == '/':
                result = result / operand[operand_idx]
                operand_idx += 1
                if operand[operand_idx] != 0:
                    raise ValueError("Cannot divide by zero")
            elif operator[operator_idx] == '**':
                result = pow(result, operand[operand_idx])
                operand_idx += 1
                if operand[operand_idx] < 0:
                    raise ValueError("Exponentiation by negative number is not allowed")
            operator_idx += 1
        return result
