

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n <= 0:
        raise ValueError
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            n //= divisor
        else:
            divisor += 1
    return divisor

