def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    #Dive into the factorization process until there is only one factor left, this factor will be the largest prime factor
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n //= i
        if n == 1:
            return i
    return n