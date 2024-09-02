

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Divisors are always <= sqrt(n)
    divisor = int(n ** 0.5)
    # Now, we check the other numbers that are potentially divisors.
    while divisor > 1:
        if n % divisor == 0:
            return divisor
        divisor -= 1
    return 1

