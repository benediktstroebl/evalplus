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
    # ----------------------
    # find prime factors
    # ----------------------
    # create set of primes numbers from 2 to n-1
    primes = [2]
    for i in range(3, n, 2):
        if n % i == 0:
            primes.append(i)

    # factorize
    prime_factors = []
    for prime in primes:
        n_prime = 0
        while n % prime == 0:
            n_prime += 1
            n //= prime
        if n_prime > 0:
            prime_factors.append(n_prime)

    # ----------------------
    # return result
    # ----------------------
    return prime_factors
