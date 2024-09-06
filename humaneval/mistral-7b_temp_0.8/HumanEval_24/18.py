

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # A naive way to solve this
    # The loop runs from 1 to n
    # If n is evenly divisible by m, return m
    # If m is larger than n, then we know that it is the largest divisor
    for m in range(1, n + 1):
        if n % m == 0:
            return m
    return n

