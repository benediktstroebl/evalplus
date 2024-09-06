def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Write n as 2^a * 3^b * 5^c * ... * p_k^z
    # Where p_k is the largest prime factor
    z = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            z += 1
            while n % i == 0:
                n //= i
        # Note if n == 2, the loop will terminate without covering all factors
        if z > 0 and n == 1:
            break
    else:
        return n  # n is a prime
    return i