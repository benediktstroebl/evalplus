

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # First, find the factors of n
    factors = [i for i in range(1, n + 1) if n % i == 0]

    # Sort the factors in descending order
    factors.sort(reverse=True)

    # Find the largest factor
    largest_factor = factors[0]

    # If there are no factors, return 1
    if len(factors) == 0:
        return 1

    # Find the largest factor that is less than or equal to n
    for i in range(1, len(factors)):
        if largest_factor > n and largest_factor % n == 0:
            largest_factor = factors[i]

    return largest_factor