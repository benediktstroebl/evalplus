def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Test if n is a prime number
    if n == 2 or n == 3:
        return n
    elif n <= 1 or n % 2 == 0 or n % 3 == 0:
        return 2
    i = 5
    while i * i <= n:
        # Check if i is a prime or not
        if n % i == 0 or n % (i + 2) == 0:
            return i
        i += 6
    # If no prime factors are found, return n
    return n