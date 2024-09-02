

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    while True:
        divisor = n // 2
        if divisor == n % divisor:
            return divisor
        else:
            n = divisor

    return n
