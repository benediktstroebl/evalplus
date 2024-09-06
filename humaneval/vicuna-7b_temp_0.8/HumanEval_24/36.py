

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Check if n is 1
    if n == 1:
        return 1
    
    # Check if n is prime
    if n > 1 and not n % 2 == 0:
        return n
    
    # Find the largest divisor
    while True:
        d = 2
        while d <= n // 2:
            if n % d == 0:
                break
            d += 1
        if n % d == 0:
            return d
    return None  # No divisor found