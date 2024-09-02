

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n <= 1:
        return 1

    largest = 0

    for divisor in range(2, n // 2 + 1):
        if n % divisor == 0:
            largest = divisor
    return largest

