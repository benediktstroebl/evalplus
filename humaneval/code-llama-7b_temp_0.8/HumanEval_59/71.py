

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    if n == 2:
        return n
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 2:
        prime_factors.append(n)
    return max(prime_factors)
