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
    # Check if the number is prime
    if n > 1:
        # if the number is not prime, return an empty list
        if n % 2 == 0:
            return []
        # Find all divisors of n
        divisors = [2]
        while n % divisors[0] == 0:
            divisors.append(divisors[divisors.index(divisors[0])] * 2)
        # Find the smallest prime factor of n
        prime_factor = 2
        while n % prime_factor == 0:
            prime_factor += 2
        # Find the second smallest prime factor of n
        prime_factor2 = 5
        while n % prime_factor2 == 0:
            prime_factor2 += 2
        # Return the list of prime factors
        return [prime_factor, prime_factor2]
    else:
        return []

