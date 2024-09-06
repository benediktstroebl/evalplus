def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Write n as 2^a * 3^b * 5^c * ... * p_k^l
    # Where p_k is the largest prime factor
    exponents = []
    for prime in PRIMES:
        while n % prime == 0:
            n //= prime
            exponents.append(exponents.__len__())
    if n > 1:
        exponents.append(exponents.__len__())
    # 2^a * 3^b * 5^c * ... * p_k^l
    # Therefore, return p_k
    return PRIMES[exponents.index(max(exponents))]
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]