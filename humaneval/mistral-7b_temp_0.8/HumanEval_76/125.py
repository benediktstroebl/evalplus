
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
    if x == pow(n, 1):
        return True
    elif x == pow(n, 2):
        return True
    elif x == pow(n, 3):
        return True
    elif x == pow(n, 4):
        return True
    elif x == pow(n, 5):
        return True
    elif x == pow(n, 6):
        return True
    else:
        return False
