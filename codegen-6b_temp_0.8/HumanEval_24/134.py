

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n % 2 == 0:
        return 2
    divisor: int = 3
    while divisor <= n:
        if n % divisor == 0:
            return divisor
        divisor += 2
    return n

