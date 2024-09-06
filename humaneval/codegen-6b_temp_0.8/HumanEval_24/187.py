

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisor = 1
    while divisor <= n:
        if n % divisor == 0:
            divisor_2 = divisor
            divisor = divisor + 1
        else:
            divisor = divisor + 1
    return divisor_2

