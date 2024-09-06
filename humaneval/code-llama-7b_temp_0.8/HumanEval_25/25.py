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
    if n < 2:
        return []
    prime = 2
    factorization = []
    while prime <= n:
        if n % prime == 0:
            count = 0
            while n % prime == 0:
                count += 1
                n //= prime
            factorization.append(prime)
            if count > 1:
                factorization.append(count)
        prime += 1
    return factorization

