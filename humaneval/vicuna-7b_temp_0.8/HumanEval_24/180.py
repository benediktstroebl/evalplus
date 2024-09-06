

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        return 1
    for i in range(2, n + 1):
        if n % i == 0:
            if i > largest_divisor(n // i):
                largest_divisor = i
    return largest_divisor
