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
    # implement me

    res = []
    n = abs(n)

    def get_factors(x, res):
        for i in range(2, x + 1):
            while x % i == 0:
                res.append(i)
                x = int(x / i)
        return res

    return get_factors(n, res)

    # for num in range(1, n + 1):
    #     if n % num == 0:
    #         res.append(num)
    #         n = int(n / num)
    #     else:
    #         continue
    # return res

