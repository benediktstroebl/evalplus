def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Write n as 2^a * 3^b * 5^c * ... * p_k^l
    # Then return max(a, b, c, ... , l)
    exp = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            exp += 1
            while n % i == 0:
                n //= i
    if n > 1:
        exp += 1
    return exp