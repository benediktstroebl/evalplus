

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # For each number between 1 and n (inclusive) that divides n evenly, check if it is smaller than n
    for i in range(1, n+1):
        if n % i == 0 and i < n:
            n = i
    
    return n

