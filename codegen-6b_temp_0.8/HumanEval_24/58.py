

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        return 1
    max_divisor = 1
    for i in range(2, n):
        if n % i == 0:
            divisor = i
            if divisor > max_divisor:
                max_divisor = divisor
    return max_divisor
