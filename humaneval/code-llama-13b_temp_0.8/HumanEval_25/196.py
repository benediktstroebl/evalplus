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
    prime = [1] * (n + 1)
    prime[0] = 0
    prime[1] = 0
    res = []

    for i in range(2, n + 1):
        if prime[i] == 0:
            continue
        res.append(i)
        for j in range(i * i, n + 1, i):
            prime[j] = 0
    return res

