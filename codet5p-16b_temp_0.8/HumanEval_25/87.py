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

    if n in [-1, 0, 1]:
        raise ValueError("The input number should be greater than 1.")
    if n < 0:
        return [abs(n)] + factorize(abs(n))
    result = []
    for i in range(2, n):
        if i * i > n:
            break
        if n % i == 0:
            result.append(i)
            n //= i
    result.append(n)
    return result

