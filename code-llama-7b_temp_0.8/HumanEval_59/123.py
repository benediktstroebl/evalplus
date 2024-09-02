

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    # This is a better version of the original largest_prime_factor method. It uses a dictionary to store the prime factors
    # of a number and uses that to look up the largest prime. If the dictionary doesn't have a number in it, it divides
    # the number by each number from 2 until it finds a number that is a factor.

    prime_factors = {}
    for i in range(2, n + 1):
        if i in prime_factors:
            continue
        # i is a prime number
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_factors[i] = i

    return max(prime_factors.values())

