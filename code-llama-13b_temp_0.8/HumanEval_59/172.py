

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    max_prime = 1
    prime_factors = []
    for i in range(2, n):
        if n % i == 0:
            prime_factors.append(i)
    for p in prime_factors:
        if n % p == 0:
            is_prime = True
            for q in range(2, p):
                if p % q == 0:
                    is_prime = False
                    break
            if is_prime and p > max_prime:
                max_prime = p
    return max_prime

