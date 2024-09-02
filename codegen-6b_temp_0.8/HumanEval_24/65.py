

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    has_divisors = False
    for divisor in range(2, n):
        if n % divisor == 0:
            has_divisors = True
            break

    if not has_divisors:
        return n
    else:
        return n // divisor
