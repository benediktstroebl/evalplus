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
    def get_factors(n, factors, factors_list):
        if n == 1:
            factors_list.append(1)
        else:
            for i in range(2, n):
                if n % i == 0:
                    factors_list.append(i)
                    n = n / i
                else:
                    factors_list.append(i)
                    break
            if n != 1:
                get_factors(n, factors, factors_list)
    factors = [2]
    factors_list = [1]
    get_factors(n, factors, factors_list)
    return factors_list

