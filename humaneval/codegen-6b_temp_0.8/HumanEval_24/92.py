

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    assert isinstance(n, int), 'the parameter n must be an integer'
    divisor = 1
    while divisor <= n:
        if n % divisor == 0:
            divisor += 1
        else:
            break
    return divisor - 1

