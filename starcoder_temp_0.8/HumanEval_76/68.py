
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    if n == 1:
        return False

    if x == 1:
        return True

    x_digits = [int(digit) for digit in str(x)]
    n_digits = [int(digit) for digit in str(n)]

    if len(x_digits) < len(n_digits):
        return False

    for i in range(0, len(n_digits)):
        if x_digits[i]!= n_digits[i]:
            return False
        if len(x_digits) == len(n_digits) and x_digits[i]!= n_digits[i]:
            return False
    return True
