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
    from math import sqrt

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def prime_factors(n: int) -> List[int]:
        primes = []
        while n % 2 == 0:
            primes.append(2)
            n //= 2

        for i in range(3, n, 2):
            while n % i == 0:
                primes.append(i)
                n //= i
            if is_prime(n):
                primes.append(n)
                break
        return primes

    return prime_factors(n)

