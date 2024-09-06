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
    if n < 4:
        return [1, n] if n > 1 else []

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
              103, 107, 109]
    prime_factors = []
    for i in range(0, len(primes)):
        cur_prime = primes[i]
        while n % cur_prime == 0:
            prime_factors.append(cur_prime)
            n = n / cur_prime

    return prime_factors

