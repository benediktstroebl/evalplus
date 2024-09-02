
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
        return (x == 0)

    # when n is a power of x we can write: n = x**a, where a is int
    # this is the same as: log(n,x) = a
    # now we only have to find a integer a such that log(n,x) = a
    return (x > 0) and (x ** (1 / n) == int((x ** (1 / n))))

