

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n == 1:
        return n
    elif n < 1:
        raise ValueError("n must be greater than or equal to 1")
    max_divisor = 1
    for i in range(2, n + 1):
        if n % i == 0:
            max_divisor = i
    return max_divisor

