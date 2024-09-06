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
    if n < 1:
        return []
    primes = [2]
    for i in range(3, n + 1):
        for prime in primes:
            if i % prime == 0:
                break
        else:
            primes.append(i)
    primes = primes[:-1]
    result = [0] * len(primes)
    for prime in primes:
        count = 0
        while n % prime == 0:
            n /= prime
            count += 1
        result[primes.index(prime)] = count
    return result

