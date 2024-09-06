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
    def prime_factors(n: int) -> List[int]:
        """ Helper function that calculates prime factors of given number """
        factors = []
        while n >= 1:
            if n % 2 == 0:
                n = n // 2
                continue
            if n % 3 == 0:
                n = 3 * n // 3
                continue
            for i in range(4, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    n = i
                    break
            else:
                factors.append(n)
                n = 1
        return factors
        
    factors = prime_factors(n)
    if not all(f == 1 for f in factors):
        return factors
    else:
        return [1] * len(factors)

