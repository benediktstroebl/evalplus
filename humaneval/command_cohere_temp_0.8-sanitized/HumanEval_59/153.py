def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Define function and main logic
    def is_prime(m):
        """Check if m is prime."""
        if m < 2:
            return False
        for i in range(2, int(m ** 0.5) + 1):
            if m % i == 0:
                return False
        return True
    
    # Iterate through numbers from 2 to n
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            return i
    return n  # If no factors found, return n