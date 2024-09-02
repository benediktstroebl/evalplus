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
    if n < 2:
        return []

    # Initialize list with number of factors of 2, and list of factors of n
    two_factors = [1]
    remaining_factors = [1]

    while remaining_factors:
        # Calculate number of factors of remaining numbers
        factors = 1
        while n % factors:
            factors *= factors
        factors = factors * (n // factors)
        # Add factors of 2 and remove factors of 2 from remaining numbers
        two_factors += [2]
        while factors // 2 == factors // 2:
            factors = factors / 2
        # Add remaining factors to list
        remaining_factors.remove(factors)

    # Return list of prime factors in the order from smallest to largest
    return two_factors[:-1] + [remaining_factors[0]]

