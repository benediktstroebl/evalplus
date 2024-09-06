
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
    if not isinstance(x, int) or not isinstance(n, int):
        raise TypeError("x and n must be integers.")
    if x < 0:
        raise ValueError("x must be a non-negative integer.")
    if n < 1:
        raise ValueError("n must be a positive integer.")

    return math.log(x, n) % 1 == 0

