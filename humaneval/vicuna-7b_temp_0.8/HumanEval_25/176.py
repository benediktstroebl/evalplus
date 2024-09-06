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
        # Check if n is prime using Sieve of Eratosthenes
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = sieve[2] = False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                sieve[i] = True
                break
        for i in range(n+1, int(n**0.5) + 1, i):
            sieve[i] = False
        prime_factors = [i for i in range(n+1) if sieve[i]]
        return prime_factors
    else:
        return []
