

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # check if n is a prime
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return i
        return n
    # check if n is a perfect square
    if n == int(n**2):
        return int(n**2)
    # check if n is a Mersenne prime
    if n == 2**n - 1:
        return n - 1
    # return the largest prime factor found so far
    return max(largest_prime_factor(n//i) for i in range(2, int(n**0.5) + 1)) + 1