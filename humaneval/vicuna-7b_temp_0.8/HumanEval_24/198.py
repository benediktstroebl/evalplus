

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # base case: if n is 1, return 1
    if n == 1:
        return 1
    
    # find the largest integer that divides n
    largest = 1
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            largest = max(largest, d)
    
    return largest
