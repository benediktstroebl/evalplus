

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n <= 1:
        raise ValueError('n must be greater than 1')
    elif n == 2:
        return n
    elif n % 2 == 0:
        return largest_prime_factor(n//2)
    else:
        max_prime = 0
        for prime in range(3,n,2):
            while n % prime == 0:
                n //= prime
                if prime > max_prime:
                    max_prime = prime
        if n > max_prime:
            max_prime = n
        return max_prime



