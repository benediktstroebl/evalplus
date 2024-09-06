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
    def check(candidates):
        """ Returns True if there is an odd number of elements in candidates that are co-prime. """
        for x, y in candidates:
            if y % x == 0:
                return False
        return True

    factors = [i for i in range(1, n+1)]
    even_factors = [i for i in factors if i % 2 == 0]
    odd_factors = [i for i in factors if i % 2 != 0]

    if len(even_factors) % 2 == 1:
        return [2] * (len(even_factors)//2)
    for candidate in odd_factors:
        if check(candidate):
            prime_factors = []
            for factor in factors:
                if factor != candidate and factor % candidate == 0:
                    prime_factors.append(factor)
            if len(prime_factors) == 2:
                return prime_factors
    return []

