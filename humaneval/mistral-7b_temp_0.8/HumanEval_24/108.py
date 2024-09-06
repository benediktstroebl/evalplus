

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    n_divisors = []
    for i in range(1, n):
        if n % i == 0:
            n_divisors.append(i)

    return n_divisors[-1]
