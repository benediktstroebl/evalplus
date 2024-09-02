

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 0:
        raise ValueError("largest_divisor input must be a positive number")

    largest_divisor = -1
    i = 2

    while i * i <= n:
        if n % i == 0:
            largest_divisor = i
            n //= i
        else:
            i += 1

    if n > 1:
        largest_divisor = n

    return largest_divisor

