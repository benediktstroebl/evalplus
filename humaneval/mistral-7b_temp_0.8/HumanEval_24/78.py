

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n < 1:
        raise ValueError(f"{n} is not a valid number")

    divisor = 1
    while divisor <= n:
        if n % divisor == 0:
            return divisor
        divisor += 1

