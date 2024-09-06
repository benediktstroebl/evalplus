

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Ensure n is a positive number
    if n <= 0:
        raise ValueError("n must be a positive value")

    # If n is 1, then there are no divisors, return 1
    if n == 1:
        return 1

    # Try decreasing numbers from n-1 down to 2
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return i

    # The only even divisor of n is 2, which is less than n
    return 2

