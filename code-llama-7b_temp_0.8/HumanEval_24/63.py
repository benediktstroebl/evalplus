

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 0:
        raise ValueError('n must be positive')
    elif n < 2:
        return 1
    else:
        for i in range(int(n**0.5), 1, -1):
            if n % i == 0:
                return i
        return n
