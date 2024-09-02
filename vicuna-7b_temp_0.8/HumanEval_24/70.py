

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Check if n is even
    if n % 2 == 0:
        # If n is even, then the largest divisor is n/2
        return n/2
    else:
        # If n is odd, then the largest divisor is the next highest odd number less than n
        for i in range(n+1, 10, -1):
            if (i+1) % 2 == 0:
                return i
        # If no divisor is found, return 10
        return 10