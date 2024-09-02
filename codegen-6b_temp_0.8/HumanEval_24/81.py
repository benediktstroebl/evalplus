

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = 0
    divisor = 1
    while divisor ** 2 <= n:
        if n % divisor == 0:
            divisors = divisors + 1
            divisor = divisor + 1
        else:
            divisor = divisor + 1

    return divisors

