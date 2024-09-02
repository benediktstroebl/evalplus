

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = []
    for d in range(1, n):
        if n % d == 0:
            divisors.append(d)
    return max(divisors)

