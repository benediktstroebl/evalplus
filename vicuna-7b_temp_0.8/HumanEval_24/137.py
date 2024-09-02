

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Check all numbers less than n
    for i in range(1, n):
        if n % i == 0:
            # If n is divisible, check if i is the largest
            if i > n // i:
                return i
    # If no number less than n is divisible, return n
    return n