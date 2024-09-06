

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 0:
        raise ValueError("n should be positive number")
    if n == 0:
        return 0
    if n == 1:
        return 1

    for num in range(2, n + 1):
        if n % num == 0:
            return num

