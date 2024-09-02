

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    if n < 2:
        return None
    else:
        n_sqrt = int(n**0.5)
        for i in range(1, n_sqrt + 1):
            if n % i == 0:
                return i
