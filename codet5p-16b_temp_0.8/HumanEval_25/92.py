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
    i = 2
    while i * i <= n:  # while i * i <= n (it's not > because it's the largest factor)
        if n % i:
            i += 1
            continue
        result.append(i)
        n //= i  # so that we can pass next i as a start value
        while n % i == 0:
            result.append(i)
            n //= i
    result.append(n)
    return result

