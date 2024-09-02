

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        return 0
    while True:
        i = (n - 1) // 2
        if n % i == 0:
            return i
        n //= i
    return 0
