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
    factorization = []

    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            times = 0
            prime = divisor

            while prime * divisor <= n:
                if n % prime == 0:
                    n /= prime
                    times += 1
                else:
                    break
            if n == 1:
                break
            factorization.append(times)
            divisor += 1

    if len(factorization) == 0:
        factorization.append(1)

    return factorization

