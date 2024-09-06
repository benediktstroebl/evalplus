

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    n_sorted = sorted(str(n))
    for i in range(len(n_sorted)):
        if n % int("".join(n_sorted[:i])) == 0:
            return int("".join(n_sorted[:i]))

