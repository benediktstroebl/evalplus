

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest = 0
    for divisor in range(1, n):
        if n % divisor == 0:
            largest = divisor
    return largest
