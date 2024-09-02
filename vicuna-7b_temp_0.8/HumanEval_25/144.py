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
    def nth_prime(n: int) -> int:
        """ Given integer n, return the nth prime number"""
        i = 1
        while n % i:
            i += 1
        return i

    prime_numbers = [nth_prime(n) for n in range(1, int(sqrt(n)) + 1)]

    factors = []
    for p in prime_numbers:
        while n % p:
            n //= p
            factors.append(p)
            n %= p
    factors = [f for f in factors if f != 1]
    return factors