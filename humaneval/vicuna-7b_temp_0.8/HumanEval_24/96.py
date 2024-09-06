

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for divisor in divisors:
        if n % divisor == 0:
            return divisor
        else:
            return divisors[0] if divisor == 1 else divisor