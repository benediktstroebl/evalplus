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
    def get_factors(n: int) -> List[int]:
        factors = []
        while n > 1:
            for i in range(1, n):
                if n % i == 0:
                    break
            n = i
            factors.append(n)
        return factors

    factors = get_factors(n)
    prime_factors = []
    for i in factors:
        while i > 1:
            p = i
            while i % p == 0:
                p += 1
            if p == 2:
                prime_factors.append(p)
            else:
                prime_factors.append(2 * p)
        for j in range(i, n, (i - j) % 2):
            if (j + 1) % 2 == 0:
                prime_factors.append(2 * j + 1)
            else:
                prime_factors.append(2 * j + 2)
    return prime_factors
