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
    res = []
    while n % 2 == 0:
        res.append(2)
        n //= 2
    primes = [3, 5]
    i = 0
    while i < len(primes):
        p = primes[i]
        while n % p == 0:
            res.append(p)
            n //= p
        i += 1
        if i == len(primes):
            primes.append(primes[i - 1] + 2)
    if n > 2:
        res.append(n)
    return res

