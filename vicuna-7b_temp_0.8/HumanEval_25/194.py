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
    def is_prime(n: int) -> bool:
        """
        Returns True if n is prime, else False.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n: int) -> List[int]:
        """
        Returns list of prime factors of n, except for the largest prime factor.
        """
        factors = []
        p = 2
        while p <= n:
            if is_prime(n - p):
                factors.append(p)
                n //= p
            p += 1
        n_factors = len(set(factors))
        return [factors[i] for i in range(n_factors)]

    n_factors = len(set(get_factors(n)))
    factors = get_factors(n)

    if n_factors == 1:
        return [factors[0]]

    factors = sorted(factors, key=lambda x: n // x)
    result = []
    for factor in factors:
        count = 1
        while factor * count <= n:
            count *= factor
        result.append(count)

    result.append(n)
    return result
