from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    from math import sqrt

    factors = []
    # For each of the number since we know the product is the same
    for x in range(2, n + 1):
        # If it's a prime
        if is_prime(x):
            # If it's our first prime factor
            if len(factors) == 0:
                factors.append(x)
            # If it's a new prime factor
            elif not x % factors[-1] == 0:
                factors.append(x)

        # If we find a multiple of our most recent prime factor
        if len(factors) > 1 and x % factors[-1] == 0:
            # Remove it from the factorization
            factors.pop(-1)
            # Get the new factor
            factors.append(x // factors[-1])

    # Make sure smallest is the first in the list
    factors = [factors[-1]] + factors[:-1]

    return factors

