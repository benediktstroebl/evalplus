

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for d in range(1, n+1):
        if n % d == 0 and d!= n:
            return d
    return
