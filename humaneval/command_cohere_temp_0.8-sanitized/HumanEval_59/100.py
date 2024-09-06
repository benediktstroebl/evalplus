def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Test if n is 2 or 3, these are the smallest prime numbers
    if n == 2 or n == 3:
        return n
    # Check if n is divisible by 2 or 3, the smallest prime numbers
    while n % 2 == 0 or n % 3 == 0:
        if n % 2 == 0:
            n //= 2
        elif n % 3 == 0:
            n //= 3
    # Check for prime factors from 5 to sqrt(n)
    for i in range(5, int(n**0.5) + 1, 6):
        while n % i == 0:
            n //= i
    # If n has reached 1, it means it was a prime number
    if n == 1:
        return n
    # In the unlikely event that n is a prime factor greater than sqrt(n)
    while n % 5 == 0:
        n //= 5
    # If n is still greater than 2, it must be a prime number
    if n > 2:
        return n
    return 2  # Return 2 if n is 2