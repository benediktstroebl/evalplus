

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    for i in range(1, int(n/2)+1):
        if n%i == 0:
            # divide until a number that isn't divisible
            while n % i == 0:
                n //= i
        else:
            return i
