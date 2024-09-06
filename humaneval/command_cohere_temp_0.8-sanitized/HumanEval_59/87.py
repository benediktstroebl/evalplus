def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Handle the case of single-digit numbers
    if n <= 10:
        if n == 2 or n == 3 or n == 5:
            return n
        return None

    # Check from sqrt(n) up to n for prime factors
    for potential_factor in range(sqrt(n), n + 1):
        if n % potential_factor == 0 and is_prime(potential_factor):
            return potential_factor

    return None
def is_prime(n):
    """Check if n is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True