

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    if n <= 0:
        raise ValueError("Number must be positive")

    divisor = 1
    for i in range(divisor, n):
        if i % divisor == 0:
            return divisor

        divisor += 1
