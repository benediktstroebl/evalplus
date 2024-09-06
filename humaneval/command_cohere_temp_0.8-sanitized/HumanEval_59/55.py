def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Your code here. Make sure to use reasonably efficient algorithms, e.g., trial division
    # Avoid brute-force factors like n // 2 until n == 1.
    largest_factor = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            largest_factor = i
            while n % i == 0:
                n //= i
        # Move ahead if the remainder is not divisible by i
        if n == 1:
            break
    return largest_factor if n == 1 else -1  # Return -1 if n is a prime