

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    n += 1
    while n > 1:
        divisor = n
        while n % divisor == 0:
            n //= divisor
        if n > 1:
            divisor += 1
        else:
            break
    return divisor