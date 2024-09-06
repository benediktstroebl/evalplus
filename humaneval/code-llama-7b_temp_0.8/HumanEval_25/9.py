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
    if n <= 0:
        raise ValueError("Only positive numbers are allowed")
    if n == 1:
        return []
    result = []
    k = 2
    while k * k <= n:
        if n % k != 0:
            k += 1
        else:
            n //= k
            result.append(k)
    if n > 1:
        result.append(n)
    return result

