

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest_divisor = 1

    for number in range(2, n):
        if n % number == 0:
            largest_divisor = number

    return largest_divisor
