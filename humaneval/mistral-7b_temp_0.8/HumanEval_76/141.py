
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
        return x == 1
    if n == 2:
        return x == 1 or x == 2 or x == 4
    if n == 3:
        return x == 1 or x == 2 or x == 3 or x == 4 or x == 8
    if n == 4:
        return x == 1 or x == 2 or x == 4 or x == 8 or x == 16
    if n == 5:
        return x == 1 or x == 2 or x == 4 or x == 8 or x == 16 or x == 32
    if n == 6:
        return x == 1 or x == 2 or x == 3 or x == 4 or x == 6 or x == 8 or x == 9 or x == 12 or x == 16 or x == 24
    if x % n == 0:
        return True
    return False
