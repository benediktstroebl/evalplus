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
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True

    prime_factors = []
    while n % 2 == 0:
        n /= 2
        prime_factors.append(2)
    i = 3
    while i <= n ** 0.5:
        while n % i == 0:
            n /= i
            prime_factors.append(i)
        i += 2
    if n > 2:
        prime_factors.append(n)
    return sorted(prime_factors)

