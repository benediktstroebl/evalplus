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
    if n < 2:
        raise ValueError("No prime factorization possible for a number less then 2")
    if n == 2:
        return [2]
    if n % 2 == 0:
        return [2] + factorize(n // 2)
    i = 3
    prime_factors = []
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
            if n == 1:
                break
        else:
            i += 2
    if n > 1:
        prime_factors.append(n)
    return prime_factors

