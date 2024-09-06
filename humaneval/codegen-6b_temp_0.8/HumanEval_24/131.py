

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest_divisor = 1  # should probably be the smallest divisor

    while n % largest_divisor != 0:
        divisor = 1

        while (n % divisor) != 0:
            divisor += 1

        if divisor > largest_divisor:
            largest_divisor = divisor

    return largest_divisor

