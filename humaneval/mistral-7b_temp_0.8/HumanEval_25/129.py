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
    # 1. if not divisible by any primes:
    if n % 2 == 0:
        return [2] + factorize(n // 2)
    if n % 3 == 0:
        return [3] + factorize(n // 3)
    if n % 5 == 0:
        return [5] + factorize(n // 5)
    if n % 7 == 0:
        return [7] + factorize(n // 7)
    # 2. all divisible by 2, but not 3, 5, 7
    elif n % 2 == 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
        return [2, 2] + factorize(n // 2)
    # 3. all divisible by 3, but not 2, 5, 7
    elif n % 2 != 0 and n % 3 == 0 and n % 5 != 0 and n % 7 != 0:
        return [
