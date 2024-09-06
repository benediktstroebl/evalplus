

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Try to find the largest divisor using trial division
    if n % 2 == 0:
        # If n is even, check if it is divisible by 2, then 4, then 8, etc.
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return i
        return n
    else:
        # If n is odd, check if it is divisible by 3, then 5, then 7, etc.
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return i
        return n
