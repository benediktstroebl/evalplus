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
    result = []
    while n % 2 == 0:
        n = n // 2
        result.append(2)
    # See: https://en.wikipedia.org/wiki/Trial_division
    # instead of checking up to sqrt(n) we can check up to n
    i = 3
    while i <= n:
        while n % i == 0:
            n = n // i
            result.append(i)
        i += 2
        if i * i > n:
            break
    if n > 1:
        result.append(n)
    return result

