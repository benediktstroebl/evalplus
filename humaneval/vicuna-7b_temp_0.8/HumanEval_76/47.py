
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
    if n < 1 or not n % 1 == 0:
        return False
    if n == 1:
        return True
    x = int(x)
    if n == x:
        return True
    if n < x:
        return False
    for i in range(2, int(log(n) / log(2)) + 1):
        if n % i == 0:
            if n // i == x:
                return True
    return False
