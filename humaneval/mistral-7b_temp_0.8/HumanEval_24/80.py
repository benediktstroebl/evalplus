

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisor = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i > divisor:
                divisor = i
    return divisor

