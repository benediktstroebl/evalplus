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
    # pre-calculating all prime numbers less than sqrt(n)
    primes = [2]
    while n % primes[0] == 0:
        primes.append(primes[0] * 2)

    factors = []
    for i in range(1, len(primes)):
        for j in range(i, len(primes)):
            if primes[i] == primes[j] * 2:
                del primes[i:j]
                break
        if primes[i] > n:
            return factors
        n_factors = 1
        while n % primes[i]:
            n_factors *= primes[i]
            n //= primes[i]
        factors.append((n_factors, primes[i]))
        n_factors = 1
        for j in primes[i:]:
            n_factors *= j
        n_factors //= primes[i]
        factors.append((n_factors, j))

    return factors

