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
    # Check if the number is a prime number
    if n < 2:
        raise ValueError("n should be a positive integer")
    if n % 2 == 0:
        return []
    # Make a list of primes up to sqrt(n)
    primes = [p for p in range(2, int(n ** 0.5) + 1) if n % p == 0]
    # Create a map of prime factors
    prime_factors = {}
    for p in primes:
        prime_factors[p] = 1
    # Keep track of number of times each factor appears
    count = {}
    for i in range(1, n + 1):
        for j in range(n, i + 1):
            if i % j == 0:
                for k in primes:
                    if j % k == 0:
                        count[k] += 1
    # Sort the prime factors by the number of times they appear
    prime_factors = sorted(prime_factors, key=lambda x: count[x], reverse=True)
    # Return the list of prime factors
    return [prime_factors.get(p, 0) for p in prime_factors]

