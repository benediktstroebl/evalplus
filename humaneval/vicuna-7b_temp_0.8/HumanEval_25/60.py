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
        Returns True if n is prime, False otherwise
        """
        if n == 2:
            return True
        elif n % 2 != 0:
            return False
        else:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

    def get_factors(n: int) -> List[int]:
        """
        Returns list of factors of n
        """
        if n == 2:
            return [2]
        else:
            factors = [n]
            while n > 1:
                for i in range(2, int(n ** 0.5) + 1, 2):
                    if is_prime(i):
                        for j in range(n // i, n - i + 1, 2):
                            factors.append(i * j)
                        n = n - i * j
                        break
            return factors

    factors = get_factors(n)
    result = []
    for factor in factors:
        count = 1
        while factor * count != n:
            count *= factor
        result.append(factor * count)

    return result

