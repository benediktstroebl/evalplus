

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # We can start at 2, as 2 divides every number evenly
    divisor = 2
    # Keep checking while divisor is a factor of n
    while n % divisor == 0:
        # If it is, update the divisor
        divisor = divisor + 1
    # Return the new divisor
    return divisor - 1
