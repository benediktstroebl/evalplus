
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
    def _digit(n):
        """
        Return the digit(s) that n has.

        Example:
        n = 432, return 2
        n = 91, return 1
        """
        return floor(log10(n)) + 1

    def _make_power(base, power):
        self = []
        for i in xrange(power):
            self += [base]
        return self

    def _addition(l1, l2):
        return [sum(x) for x in zip(l1, l2)]

    def _subtract(l1, l2):
        return [x[0] - x[1] for x in zip(l1, l2)]

    def _fold(l):
        return reduce(lambda x, y: x + y, l)

    def _divide(l1, l2):
        return [x[0] / x[1] for x in zip(l1, l2)]

    def _floor_divide(l1, l2):
        return [floor(x[0] / x[1]) for x in zip(l1, l2)]

    def _exponent(l1, l2):
        return [x[0] ** x[1] for x in zip(l1, l2)]

    operator_mapper = {
        '+': _addition,
        '-': _subtract,
        '*': _fold,
        '/': _divide,
        '//': _floor_divide,
        '**': _exponent,
    }

    operator_idx = 0
    sum_result = 0
    for i in xrange(len(operand) - 1):
        if operator[operator_idx][0] == '+':
            sum_result += operand[i]
        elif operator[operator_idx][0] == '-':
            sum_result -= operand[i]
        elif operator[operator_idx][0] == '*':
            sum_result *= operand[i]
        elif operator[operator_idx][0] == '//':
            sum_result //= operand[i