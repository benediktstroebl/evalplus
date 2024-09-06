

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # find the largest number that divides n evenly
    i = 2
    while n % i != 0:
        i += 1
    i -= 1

    # recurse if i is not a prime
    if largest_prime_factor(i) != i:
        return largest_prime_factor(i)

    # return i if i is a prime
    return i

