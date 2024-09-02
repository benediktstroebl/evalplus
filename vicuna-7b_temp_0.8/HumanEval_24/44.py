

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Try each number from 2 to n-1
    for i in range(2, n+1):
        # If n is evenly divisible by i, return i
        if (n // i) == i:
            return i
    # If n is not evenly divisible by any number from 2 to n-1, return n
    return n
