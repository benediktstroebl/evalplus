
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
    def to_int(num):
        return int(num)

    def to_float(num):
        return float(num)

    def to_str(num):
        return str(num)

    def add(nums, val):
        return reduce(lambda x, y: x + y, nums) + val

    def subtract(nums, val):
        return reduce(lambda x, y: x - y, nums) + val

    def multiply(nums, val):
        return reduce(lambda x, y: x * y, nums) + val

    def floordiv(nums, val):
        return reduce(lambda x, y: x // y, nums) + val

    def exp(nums, val):
        return reduce(lambda x, y: x ** y, nums) + val

    def divide(nums, val):
        return reduce(lambda x, y: x / y, nums) + val

    if operator == '+':
        return add(operand, operand[len(operand) - 1])
    elif operator == '*':
        return multiply(operand, operand[len(operand) - 1])
    elif operator == '-':
        return subtract(operand, operand[len(operand) - 1])
    elif operator == '//':
        return floordiv(operand, operand[len(operand) - 1])
    elif operator == '**':
        return exp(operand, operand[len(operand) - 1])
    elif operator == '/':
        return divide(operand, operand[len(operand) - 1])
    else:
        return None
