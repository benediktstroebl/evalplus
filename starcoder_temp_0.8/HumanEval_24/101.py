

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        raise ValueError(f'Cannot divide by {n}')
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n = n // divisor
        else:
            divisor += 1
    return n
