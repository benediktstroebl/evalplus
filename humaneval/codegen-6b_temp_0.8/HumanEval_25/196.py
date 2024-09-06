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
    # import math
    # if n < 0:
    #     n = -n
    # if n == 1:
    #     return [1]
    # if n == 0:
    #     return []
    # elif n == 2:
    #     return [2]
    # for i in range(2, int(math.sqrt(n)) + 1):
    #     if n % i == 0:
    #         count = 0
    #         if i ** 2 == n:
    #             count += 1
    #         else:
    #             while n % i == 0:
    #                 count += 1
    #                 n //= i
    #         return [i] * count + factorize(n)
    # return [n]

    # key = 9999999
    # factors = []
    # if n < 0:
    #     n = -n
    # while n > 1:
    #     res = factor(n)
    #     if res[0] < key:
    #         key = res[0]
    #         factors = res[1]
    #     n //= res[0]
    # return [key] + factors

    # for p in sieve(100):
    #     if p * p > n:
    #         break
    #     if n % p == 0:
    #         yield p
    #     n //= p
    # if n > 1:
    #     yield n

    factors = []
    for p in sieve(n):
        if p > n:
            break
        if n % p == 0:
            factors.append(p)
            yield p
            n //= p
    if n > 1:
        factors.append(n)
        yield n

    return factors

