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
    if n <= 1:
        return []
    if n == 2:
        return [2]
    if n % 2 == 0:
        return [2] * int(n / 2)
    if n % 3 == 0:
        return [3] + factorize(n // 3)
    result = []
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0:
            result.extend([i, n // i])
    return
