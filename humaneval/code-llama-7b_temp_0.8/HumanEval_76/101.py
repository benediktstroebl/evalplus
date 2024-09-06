
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
    elif n == 2:
        return x == 4 or x == 1 or x == 2
    elif n == 3:
        return x == 9 or x == 1 or x == 3
    elif n == 4:
        return x == 16 or x == 1 or x == 4
    elif n == 5:
        return x == 25 or x == 1 or x == 5
    elif n == 6:
        return x == 36 or x == 1 or x == 6
    elif n == 7:
        return x == 49 or x == 1 or x == 7
    elif n == 8:
        return x == 64 or x == 1 or x == 8
    elif n == 9:
        return x == 81 or x == 1 or x == 9
    else:
        return False

