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
    prime_factors = []
    # Go through all the prime numbers less than n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            # If n is divisible by prime i, then we need to check if we can divide n by any smaller prime factor of i
            for j in range(i, int(n ** 0.5) + 1):
                if n // j == 0:
                    # If n can be divided by any smaller prime factor of i, then n is not prime and we return the list of prime factors
                    return [i]
            # If we can't divide n by any smaller prime factor of i, then n is prime
            prime_factors.append(i)
    # If we get here, we know that n is prime and we return an empty list
    return []

