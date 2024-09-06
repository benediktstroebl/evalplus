

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 1:
        return 0
    divisors = []
    for d in range(1, n + 1):
        for i in range(n // d, n - d + 1):
            if n % i == 0:
                divisors.append(d)
    return max(divisors)
