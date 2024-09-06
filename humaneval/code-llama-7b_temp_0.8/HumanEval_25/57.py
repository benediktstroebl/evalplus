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
    if n == 1:
        return [1]

    # Divide by 2 until it is odd, then divide by all other odd numbers until it is prime
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    def is_prime(num):
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    for i in range(3, n, 2):
        if is_prime(i) and n % i == 0:
            factors.append(i)
            while n % i == 0:
                factors.append(i)
                n //= i

    return factors

