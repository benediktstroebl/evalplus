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
    if n < 0:
        return []

    if n == 0:
        return [1]

    if n in prime_numbers:
        return [n]

    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
        factors.append(i)

    for i in range(1, len(factors)):
        for j in range(i + 1, len(factors)):
            if factors[i] * factors[j] == n:
                for k in range(i + 1, len(factors)):
                    factors[k] = factors[k] * (factors[i] * factors[j])
                for k in range(j - 1, -1, -1):
                    factors[k] = factors[k] * (factors[i] * factors[j])
                break

    for k in range(i, len(factors)):
        for j in range(0, i):
            factors[j] = factors[j] * (factors[i])
        for j in range(i + 1, len(factors)):
            factors[j] = factors[j] * (factors[i] * factors[j])
        break

    return factors

