

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # Base case
    if n <= 1:
        return n

    # Make a list of divisors
    divisors = [i for i in range(2, n) if n % i == 0]

    # If there are no divisors, the largest divisor is 1
    if len(divisors) == 0:
        return 1

    # Else, find the largest divisor
    return divisors[-1]

