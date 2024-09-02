

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]
    while len(divisors) < n:
        divisors.extend(range(1, 16))
    while n % divisor for divisor in divisors:
        if n % divisor == 0:
            return divisor
    return 15
