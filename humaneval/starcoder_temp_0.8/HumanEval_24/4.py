

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        return n
    divisor = 1
    while divisor * divisor <= n:
        divisor += 1
        if n % divisor == 0:
            return divisor
