

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Find the largest factor of the number
    for x in range(n - 1, 1, -1):
        if n % x == 0:
            return x

