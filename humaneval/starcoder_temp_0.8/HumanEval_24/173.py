

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n <= 1:
        return 1
    div = 2
    while div * div <= n:
        if n % div == 0:
            n //= div
        else:
            div += 1
    return n

