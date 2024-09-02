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
    prime_numbers = [True] * (n + 1)
    prime_numbers[0] = False
    prime_numbers[1] = False
    prime_numbers[2] = True
    prime_numbers[3::2] = [False] * len(prime_numbers[3::2])
    prime_factors = []
    for i in range(2, n + 1):
        if prime_numbers[i]:
            prime_factors.append(i)
            prime_numbers[i * i : : i] = [False] * len(prime_numbers[i * i : : i])
    result = []
    for prime_factor in prime_factors:
        while n % prime_factor == 0:
            n //= prime_factor
            result.append(prime_factor)
    if n > 1:
        result.append(n)
    return result

