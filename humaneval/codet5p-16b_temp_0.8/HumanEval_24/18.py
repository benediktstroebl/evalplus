

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    largest_divisor_n = 0
    for i in range(1, n + 1):
        if n % i == 0 and i > largest_divisor_n:
            largest_divisor_n = i
    return largest_divisor_n

