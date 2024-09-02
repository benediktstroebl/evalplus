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

    # Factors of 1 are not prime
    while n % 2 == 0:
        prime_factors.append(2)
        n = n / 2

    # Keep looping until n is 1
    while n > 1:
        # Loop through the factors up to square root of n
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            # If n is divisible by i then n/i is a factor of n
            if n % i == 0:
                prime_factors.append(i)
                n = n / i
                break

        # n is prime
        else:
            prime_factors.append(int(n))
            break
    return prime_factors

