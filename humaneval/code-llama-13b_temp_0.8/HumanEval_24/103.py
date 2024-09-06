

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # When n is 1, 0 divides n evenly
    if n <= 1:
        return 0
    
    # Iterate from n // 2 to 1 to find a divisor
    for divisor in range(n // 2, 0, -1):
        if n % divisor == 0:
            return divisor
    
    return 1

