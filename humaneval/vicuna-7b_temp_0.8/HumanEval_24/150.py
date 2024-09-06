

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Find all divisors of n
    divisors = [i for i in range(1, n + 1) if n % i == 0]

    # Find the largest divisor and check if it is smaller than n
    largest_divisor = max(divisors)
    if largest_divisor >= n:
        return -1
    else:
        return largest_divisor
