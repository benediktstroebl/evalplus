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
    primes = [2, 3, 5]
    if n <= 3:
        return [n]
    # make sure n is odd
    n, is_even = n >> 1, n & 1 << 1
    for i in range(6, n + 1, 6):
        primes.extend([i - 1, i + 1, i + 5])
    factors = []
    for p in primes:
        while n % p == 0:
            n //= p
            factors.append(p)
    if is_even:
        factors.append(2)
    if n > 1:
        factors.append(n)
    return factors

