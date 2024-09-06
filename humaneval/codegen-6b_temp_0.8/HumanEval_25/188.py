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
    if n == 1:
        return 1
    max_divisor = 1
    max_divisor_idx = 0
    for i in range(2, n + 1):
        if n % i == 0:
            if i * i > max_divisor:
                max_divisor = i * i
                max_divisor_idx = i
    return [max_divisor_idx, max_divisor_idx]

