
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
    operands = [operand]
    operator_product = operator[0]
    left_side = [0]
    right_side = [0]
    result = [0]
    for i in range(len(operator)):
        operator_index = operator[i]
        operand_index = operand[i]
        operator_value = operator_product[operator_index]
        operand_value = operand[i + 1]
        operator_value_neg = operator_value * (-1)
        operator_product = operator_product[:i] + operator_value + operator_product[i + 1:]
        operator_product = operator_product[:operand_index] + operator_value_neg + operator_product[operand_index + 1:]

        for j in range(i, len(operator)):
            operator_index = operator[j]
            operand_index = operand[j]
            operator_value = operator_product[operator_index]
            operand_value = operand[j + 1]
            operator_product = operator_product[:operand_index] + operator_value + operator_product[operand_index + 1:]

            if operator_value == operator_product[-1]:
                left_side.append(left_side[-1] * operator_value)
                right_side.append(operand_value)
                result.append(left_side[-1] * operand_value)
                break
            elif operator_value == operator_product[0]:
                left_side.append(left_side[-1] * operator_value)
                right_side.append(operand_value)
                result.append(left_side[-1] * operand_value)
                break
            else:
                left_side.append(left_side[-1] * operator_value)
                right_side.append(operand_value)
                result.append(left_side[-1] * operand_value)
                if operator_value == operator_product[-2]:
                    left_side.append(operator_product[-1])
                    right_side.append(operand_value)
                    result.append
