
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
    # Use a combination of multiplication and division with remainders
    # to check if x is a simple power of n
    for _ in range(1000000):
        y = n ** int(x % n)
        if y == x:
            return True
        if y != x:
            return False
    return False