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
    # We know that all numbers n greater than 1 are divisible by 1
    # (except n=1). 
    # So we can start from 2, i.e. n=2
    result = []
    n = abs(n)
    i = 2
    while i*i <= n:
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            result.append(i)
        i += 1
    if n > 1:
        result.append(n)
    return result
