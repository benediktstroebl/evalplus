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

    primes = [2]

    for i in range(3, n, 2):
        for prime in primes:
            if prime > i:
                primes.append(i)
                break
            if i % prime == 0:
                break

    factors = {}
    i = 0
    while n > 1:
        prime = primes[i]
        if n % prime == 0:
            n //= prime
            try:
                factors[prime] += 1
            except KeyError:
                factors[prime] = 1
        else:
            i += 1

    return [i for i in factors.keys()]

