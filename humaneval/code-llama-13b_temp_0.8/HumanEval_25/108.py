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
    # solution 1
    result = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            result.append(i)
        else:
            i += 1
    result.append(n)
    return result

    # solution 2
    import math

    result = []
    while n > 1:
        i = 2
        while i <= math.sqrt(n):
            if n % i == 0:
                result.append(i)
                n //= i
                break
            else:
                i += 1
        if n > 1:
            result.append(n)
    return result

    # solution 3
    i, j = 2, int(math.sqrt(n))
    result = []
    while i <= j:
        if n % i == 0:
            result.append(i)
            n //= i
        else:
            i += 1
        if n > 1 and i > j:
            j = int(math.sqrt(n))
            i = 2
    return result

    # solution 4
    i, j = 2, int(math.sqrt(n))
    result = []
    while i <= j:
        if n % i == 0:
            result.append(i)
            n //= i
        else:
            i += 1
        if n > 1 and i > j:
            j = int(math.sqrt(n))
            i = 2
    if n > 1:
        result.append(n)
    return result
