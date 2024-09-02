

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    def _is_divisible(divisor):
        return n % divisor == 0

    divisor = 1
    while not _is_divisible(divisor):
        divisor += 1
    return divisor

