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
    def get_factors(n):
        factors = []
        while n >= 1:
            if n % 2 == 0:
                factors.append(2)
            else:
                factors.append(3)
            n = n // 2
        return factors

    def get_prime_factors(n):
        factors = get_factors(n)
        prime_factors = []
        for factor in factors:
            if n % factor == 1:
                prime_factors.append(factor)
                n = n // factor
        return prime_factors

    def find_smallest_prime_factor(prime_factors):
        smallest_factor = max(prime_factors, key=lambda x: x if x > 1 else 0)
        for factor in prime_factors:
            if factor < smallest_factor:
                smallest_factor = factor
        return smallest_factor

    prime_factors = get_prime_factors(n)
    smallest_factor = find_smallest_prime_factor(prime_factors)
    result = [smallest_factor]

    for factor in prime_factors:
        for i in range(1, len(prime_factors)):
            if prime_factors[i] > factor:
                result.append(prime_factors[i])
                break
        else:
            result.append(prime_factors[i])
    return result
