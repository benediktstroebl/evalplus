

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    l = 0
    while True:
        if n % l == 0:
            return l
        l += 1
        
