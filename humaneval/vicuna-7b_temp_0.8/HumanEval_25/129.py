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
        Function to check if a given integer is prime or not
        """
        if n < 2:
            return False
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                return False
        return True

    factors = []
    for x in range(2, int(n**0.5) + 1):
        if is_prime(x):
            factors.append(x)
    if n == 1:
        return [1]
    for i in range(2, int(n**0.5) + 1):
        while (n % i == 0) and (i != n):
            n = i
            i -= 1
        if n != 1:
            factors.append(n)
    return factors

