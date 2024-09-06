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
    while primes[-1] * primes[-1] <= n:
        if n % primes[-1] == 0:
            n //= primes[-1]
            primes.append(primes[-1])
        else:
            primes.append(n)
            break
    return primes
