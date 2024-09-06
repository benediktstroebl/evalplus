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
    if not 1 <= n <= 100:
        raise ValueError("Invalid input")
    n = n - 1
    prime = [i for i in range(2, n) if n % i == 0]
    factors = []
    for p in prime:
        while p <= n:
            for i in range(p, n, p):
                factors.append(i)
                break
        factors.append(p)
        for i in range(p, n, p):
            if n % i == 0:
                break
        factors.append(n // i)
    return factors
