

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    divisors = list(range(1, n))
    largest = 1
    for d in divisors:
        if n % d == 0 and d > largest:
            largest = d
    return largest
