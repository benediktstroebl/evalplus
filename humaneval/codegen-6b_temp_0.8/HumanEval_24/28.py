

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    i = 1
    while True:
        if i > n:
            return n
        if n % i == 0:
            if i > n / i:
                return n // i
            i = n / i
        i += 1

