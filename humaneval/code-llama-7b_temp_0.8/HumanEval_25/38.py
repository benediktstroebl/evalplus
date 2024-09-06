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
    if n < 1:
        raise ValueError("Factorized number should be greater or equal to 1.")
    if n == 1:
        return [1]

    def prime_factors(n: int) -> List[int]:
        prime_factors_list = []
        i = 2
        while i ** 2 <= n:
            if n % i:
                i += 1
            else:
                n //= i
                prime_factors_list.append(i)
        if n > 1:
            prime_factors_list.append(n)
        return prime_factors_list

    return prime_factors(n)

