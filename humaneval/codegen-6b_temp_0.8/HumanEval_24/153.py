

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest_divisor = 1
    current_divisor = 1
    while current_divisor <= n:
        if n % current_divisor == 0:
            largest_divisor = current_divisor
        current_divisor += 1
    return largest_divisor
