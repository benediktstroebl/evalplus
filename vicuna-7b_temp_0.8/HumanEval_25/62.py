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
        Returns True if n is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n: int) -> List[int]:
        """
        Yields prime factors of n in the order from smallest to largest.
        """
        while True:
            if is_prime(n):
                yield n
            else:
                for d in range(n, -1, -1):
                    if n % d == 0:
                        break
                else:
                    yield n

    factors = get_factors(n)
    factors = sorted(factors, key=lambda x: x)
    result = [1]
    for factor in factors:
        result *= factor
    return [int(x) for x in result]
