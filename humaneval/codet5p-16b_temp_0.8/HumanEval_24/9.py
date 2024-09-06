

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    i = 2
    divisor = 1
    while i * divisor <= n:
        if n % i == 0:
            divisor = i
        i += 1
    return divisor
