

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    i = 1
    max_val = 1
    while i <= n:
        if n % i == 0:
            max_val = i
            break
        i += 1
    return max_val
