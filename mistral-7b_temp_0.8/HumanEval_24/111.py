

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 1:
        raise ValueError("Number must be positive!")
    for i in range(n):
        if n % i == 0 and i < n:
            return i

