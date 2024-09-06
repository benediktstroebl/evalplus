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
    primes = []
    candidate = 2
    factorization = 1
    while (n > 1) and (n % candidate != 0):
        if n % candidate == 0:
            primes.append(candidate)
        candidate += 1
    for p in primes:
        factorization *= p
    remainder = 0
    if n != factorization:
        remainder = n - factorization
    return [factorization] + factorize(remainder) if remainder > 1 else [factorization]

