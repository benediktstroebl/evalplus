

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    result = n
    for i in range(2, n):
        if n % i == 0 and n // i < n:
            result = i
    return result

