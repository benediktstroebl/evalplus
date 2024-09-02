
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
    if x == 1 and n == 1:
        return True
    if x % n == 0:
        return True
    else:
        return False


"""Part Two:

Given two positive integers x and y, write a function that returns true if x and y are
factors of x**y.

For example, 10 and 10**4 are factors of 10**4.
"""

