

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    divisors: list = []

    for x in range(1, n):
        if n % x == 0:
            divisors.append(x)

    if divisors:
        return max(divisors)
    else:
        return n

