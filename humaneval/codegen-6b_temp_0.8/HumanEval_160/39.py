
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
    def _operator(operator, operand, operator_int):
        if operator_int == 0:
            return [0] * len(operand)
        def sub(operator, operand, operator_int):
            if operator_int == 0:
                return [0] * len(operand)
            if operator_int == 1:
                return operand
            if operator_int == 2:
                return operator
            if operator_int % 2 == 0:
                return operator
            return operator[operator_int-2]
        if operator_int == len(operator)-1:
            return operator
        if operator_int % 2 == 0:
            operand = sub(operator, operand, operator_int // 2)
            return [operator[operator_int // 2] * operand[0] + operator[operator_int // 2] * operand[1],
                    operator[operator_int // 2] * operand[0] + operator[operator_int // 2] * operand[2],
                    operator[operator_int // 2] * operand[1] + operator[operator_int // 2] * operand[2]]
        return [
            operator[operator_int // 2] * sub(operator, operand, operator_int // 2)[0] +
            operator[operator_int // 2] * sub(operator, operand, operator_int // 2)[1],
            operator[operator_int // 2] * sub(operator, operand, operator_int // 2)[0] +
            operator[operator_int // 2] * sub(operator, operand, operator_int // 2)[2],
            operator[operator_int // 2] * sub(operator, operand, operator_int // 2)[1] +
            operator[operator_int // 2] * sub(operator, operand, operator_int // 2)[2]]
    return [_operator(operator, operand, i)[0] for i in range(0, len(operand)-1)][len(operand)-1]

