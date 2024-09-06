def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Handle the case where n is a power of 2.
    if n > 2 and (n & (n - 1)) == 0: 
        return 2
    # circling_sum iterates through numbers and counts their occurrences as factors
    # looping through numbers in circled_sum, the largest factor will be the last one that is not present in the list of divisors
    # where divisors are defined as numbers that divide n exactly
    circled_sum = [abs(n) // i for i in range(3, int(n ** 0.5) + 1, 2) if n % i == 0]
    divisors = [i for i in range(2, int(n ** 0.5) + 1) if n % i == 0]
    return circled_sum[-1] if circled_sum[-1] in divisors else -1