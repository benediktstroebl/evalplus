
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
    if n == 0:
        return False
    elif n == 1:
        return True
    elif n % 2 == 0:
        return is_simple_power(x % 2, 2)
    elif n % 3 == 0:
        return is_simple_power(x % 3, 3)
    elif n % 4 == 0:
        return is_simple_power(x % 4, 4)
    elif n % 5 == 0:
        return is_simple_power(x % 5, 5)
    else:
        return False
