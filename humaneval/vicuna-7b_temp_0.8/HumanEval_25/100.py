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
    # First, check if the input number is prime
    if n > 1:
        if n % 2 != 0:
            return [n]
        else:
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return []
            return [n]

    # Find all prime numbers less than or equal to n
    primes = [p for p in range(2, int(n**0.5) + 1) if n % p == 0]

    # Create a list to store the factors
    factors = []

    # Loop through the prime numbers
    for p in primes:
        # Loop through the remaining numbers
        for i in range(1, n // p):
            # Add the prime number and multiply by i
            factors.append(p)
            factors.append(i)

    return factors