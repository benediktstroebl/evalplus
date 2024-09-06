

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # if n is even, the largest divisor is half of n
    if n % 2 == 0:
        return n // 2
    
    # start with the number itself, decreasing by 1
    largest_divisor = n
    while largest_divisor >= 2:
        if n % largest_divisor == 0:
            break
        largest_divisor -= 1

    return largest_divisor

