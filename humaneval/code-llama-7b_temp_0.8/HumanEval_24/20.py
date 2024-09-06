

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # We are going to use the ceil of the square root of n, as it is the largest integer
    # that is smaller than the square root of n.
    # We are not going to check the number n itself, as it is never going to be a divisor
    upper_bound = int(n**0.5)
    for i in range(upper_bound, 1, -1):
        if n % i == 0:
            return i
    return 1
