

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # factor out all of the primes from 2 through the square root of n
    # e.g. 2048 = 2**11 = 2*2*2*2*2*2*2*2*2*2
    # and the largest prime factor is 2
    # e.g. 13195 = 3*3*5*11*17
    # and the largest prime factor is 17
    largest = 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            largest = i
            n /= i

    return largest
