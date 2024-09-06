

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def f(i: int) -> bool:
        return n % i == 0

    i = 1
    while i > 0:
        i -= 1
        if f(i):
            break
    return i

