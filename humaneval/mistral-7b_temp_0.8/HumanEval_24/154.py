

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 2:
        raise ValueError('Number is not evenly divisible by any other number')
    if n % 2 == 0:
        return 2
    for i in range(3, n + 1):
        if n % i == 0:
            return i
    raise ValueError('Number is not evenly divisible by any other number')

