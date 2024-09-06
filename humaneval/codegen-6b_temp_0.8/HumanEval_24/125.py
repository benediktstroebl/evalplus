

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 0:
        raise ValueError("Cannot calculate a divisor for a negative number")
    if n == 0:
        return 0
    if n < 1:
        return 1
    for k in range(n, 0, -1):
        if n % k == 0:
            return k
    return 1

