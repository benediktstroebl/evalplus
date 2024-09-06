def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest possible factor ax + yz where gcd(a, b) = 1
    a = b = n
    while b > 1:
        a, b = b, a % b
    # If a is a prime, that's the largest factor, otherwise n is a prime
    return a if a == 1 else n