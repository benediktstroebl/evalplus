
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
    if x < 0:
        return False
    if x == 0:
        return False
    if n < 0:
        return False

    if x == 1:
        return True

    # n is greater than 1
    if n > 1:
        # log(x, n) is a simplified form of int(x**(1/n)).
        # This turns out to be roughly the same time as int(x**(1/n)),
        # so we use that result.
        if x % n == 0:
            return True
        else:
            return False

    # n is a negative number
    elif n < 0:
        # The logarithm of x is a solution to f(x) = log(x) = 1/n.
        # However, f(x) can't be deterministically
        # exact, so we can only use this heuristics.
        if x % n == 0:
            return True
        else:
            return False
