
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
    if not isinstance(x, int):
        raise TypeError("x must be integer")

    if not isinstance(n, int):
        raise TypeError("n must be integer")

    if n < 0:
        raise ValueError("n must be positive")

    if x < 0 or x % n!= 0:
        return False
    return True

