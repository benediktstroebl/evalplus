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
    prime_factors = []
    for i in range(1, n + 1):
        for num in range(i, n + 1, i):
            for p in primes:
                if num % p == 0:
                    break
            else:
                prime_factors.append(p)
    return prime_factors

