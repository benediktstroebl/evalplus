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
    # base case
    if n <= 1:
        return [n]
    # find the smallest prime factor
    p = 2
    while p**2 <= n:
        if n % p:
            break
        p += 1
    # find the rest of the prime factors
    factors = [p]
    while p**2 <= n:
        p += 1
        for i in range(p-1, n, p):
            if not(n % i):
                break
        else:
            factors.append(p)
    # return the list of prime factors
    return factors
