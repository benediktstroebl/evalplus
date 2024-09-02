

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # Base case
    if n <= 1:
        return 1

    largest_divisor = n

    for i in reversed(range(1, n)):
        if n % i == 0:
            largest_divisor = i
            break

    return largest_divisor

