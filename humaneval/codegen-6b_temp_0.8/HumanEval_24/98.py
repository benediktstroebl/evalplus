

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    large_divisor = 1

    # Look at first few numbers, update the divisor
    for i in range(2, (n // 2) + 1):
        if (n % i) == 0:
            large_divisor = i
    
    return large_divisor
