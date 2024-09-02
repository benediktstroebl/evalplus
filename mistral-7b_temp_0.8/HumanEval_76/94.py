
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
    if x == 1:
        return True
    elif n == 1:
        return False
    elif n == 2:
        return x % 4 == 0
    else:
        if n == 3:
            return x % 8 == 0
        elif n == 4:
            return x % 16 == 0
        elif n == 5:
            return x % 32 == 0
        elif n == 6:
            return x % 64 == 0
        elif n == 7:
            return x % 128 == 0
        elif n == 8:
            return x % 256 == 0
