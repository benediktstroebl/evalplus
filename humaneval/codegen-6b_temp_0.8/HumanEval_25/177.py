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
    # if n == 1:
    #     return [1]
    # if n % 2 == 0:
    #     div = 2
    # else:
    #     div = 2
    # prime_factor = []
    # while n != 1:
    #     if div ** 2 > n:
    #         div -= 1
    #         div_sq = div ** 2
    #         div_sq = div_sq + div_sq
    #         while div_sq < n:
    #             n = n - div_sq
    #             prime_factor.append(div)
    #         prime_factor.append(n)
    #         break
    #     div += 1
    #     div_sq = div ** 2
    #     div_sq = div_sq + div_sq
    #     while div_sq < n:
    #         n = n - div_sq
    #         prime_factor.append(div)
    # prime_factor.sort()
    # return prime_factor

    import math

    if n < 2:
        return []
    if n == 2:
        return [2]
    count = 0
    step = 2
    prime_factor = []
    while n != 1:
        if n % step == 0:
            n = n / step
            count += 1
            prime_factor.append(step)
        else:
            step += 1
    return count

