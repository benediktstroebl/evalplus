
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
    # check if n is 1, or if x is equal to n**int
    if n == 1 or x == n**int:
        return True
    # check if n is even, if x is odd and n**int is even
    if n % 2 == 0 and x % 2 != 0:
        return True
    # check if n is odd, if x is even and n**int is odd
    if n % 2 != 0 and x % 2 == 0:
        return True
    # check if n is odd and x is odd and n**int is odd
    return x % 2 == 1 and n % 2 == 1