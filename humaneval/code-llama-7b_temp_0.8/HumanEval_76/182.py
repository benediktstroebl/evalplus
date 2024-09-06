
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
    if x == n:
        return True
    elif int(x) == x:
        return False
    return x ** int(x) == n ** int(x)

    # return n in range(1, int(x) + 1) and n ** int(x) == x

    # return n ** (x - int(x)) == 1 and int(x) <= n ** int(x) <= x

