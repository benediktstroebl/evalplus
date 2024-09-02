

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        return 1

    while True:
        d = (n - 1) // 2
        if n % d == 0 and d > n / 2:
            return d
        elif n % d != 0 and n // d > n / 2:
            return n
        n //= d
