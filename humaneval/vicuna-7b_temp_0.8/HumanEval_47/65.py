

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

def power(base: float, exponent: int, modulo: int):
    """Calculate the nth root of a number using the Newton-Raphson method.
    The method stops when the relative error is less than 10^(-8).

    Returns the result as a float.
    """
    while True:
        result = (base ** exponent) % modulo
        if abs(result - base ** exponent) < 10**(-8):
            break
        exponent -= 1
        base = result

    return base

def find_least_common_multiple(a: list, b: list):
    """Find the least common multiple of two or more integers.
    """
    lcm = 1
    for x in a:
        for y in b:
            if x != y:
                lcm = lcm * (x // y)
    return lcm

def find_greatest_common_divisor(a: list, b: list):
    """Find the greatest common divisor of two or more integers.
    """
    while True:
        lcm = max(a, b)
        for x in a:
            for y in b:
                if x % lcm == 0:
                    break
        if x % lcm == 0:
            return lcm
        a = x
        b = lcm
