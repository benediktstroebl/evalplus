

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Check the range of numbers that can divide n
    if n < 2:
        return 1
    if n % 2 == 0 and n != 2:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        divisor = int(n / 2)
        if n % divisor == 0:
            if n > divisor * 2:
                return divisor
        n /= 2
    return None
