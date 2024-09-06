def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Iterate through potential factors from 2 to the square root of n
    for potential_factor in range(2, int(n**0.5) + 1):
        if n % potential_factor == 0:
            return potential_factor
        # Check if the divisor is a prime number, optimizing the process
        if potential_factor in PRIMES:
            return potential_factor
        PRIMES.append(potential_factor)
    # If no factors found, return n
    return n
PRIMES = [2, 3, 5, 7]