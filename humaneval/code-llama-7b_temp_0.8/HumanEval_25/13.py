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
    # your task: replace this with factorization
    primes = [2, 3, 5, 7, 11, 13, 17]
    i = 0
    f = []
    while True:
        if n == 1:
            return f
        if i == len(primes):
            break
        while n % primes[i] == 0:
            n = n / primes[i]
            f.append(primes[i])
        i += 1
    return f

