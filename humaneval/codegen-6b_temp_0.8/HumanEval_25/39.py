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
    # factors = [1]  # the number of times that I've seen this number
    # num: int = 1
    # while num <= n:  # while we haven't seen this number already
    #     if n % num == 0:  # if we have seen this number already
    #         # times = factors[n // num]  # how many times it appeared
    #         times = n // num  # how many times it appeared
    #         if times > 1:
    #             factors.append(n // num)  # add it to results
    #         factors[n // num] += 1  # add that it appeared once more
    #         num *= num  # try adding more numbers
    #     else:  # if we haven't seen this number yet
    #         num += 1  # increment num
    # factors = [n // i for i in factors]  # reverse sort it
    # return factors
    factors = []
    factor = 2
    while factor <= n:
        if n % factor == 0:
            factors.append(factor)
            n //= factor
        else:
            factor += 1

    if n > 1:
        factors.append(n)

    return factors


from functools import reduce

