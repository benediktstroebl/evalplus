

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    k = n
    while k > 1:
        if n % k == 0:
            return k
        k -= 1
    return 1


