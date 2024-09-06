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
    # Check if n is prime
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return []
        return [i]

    # Check if n is even
    if n % 2 == 0:
        return [2]

    # Check if n is odd
    odd_factors = [i for i in range(3, int(n ** 0.5) + 1) if n % i == 0]

    # If no odd factors, then n is prime
    if not odd_factors:
        return [1]

    # Find the largest odd factor
    max_odd_factor = max(odd_factors)

    # Find the smallest factor larger than max odd factor
    min_even_factor = min(even_factors)

    # If there is no even factor, then n is prime
    if min_even_factor is None:
        return [1]

    # Otherwise, n is composite, so we return a list of the factors in the order from smallest to largest
    return [min_even_factor, max_odd_factor]

