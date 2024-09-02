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
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
    factors = []
    for prime in prime_numbers:
        if n % prime == 0:
            factors.append(prime)
            n //= prime
    return factors

