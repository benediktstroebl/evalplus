def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Handle the case where n is a power of 2.
    if n >= 2 and ((n & (n - 1)) == 0):
        return 2
    # Traverse through the list of prime numbers from `prime_list` and return the largest prime factor.
    for prime in PRIME_LIST:
        while n % prime == 0:
            n //= prime
        if n == 1:
            return prime
    # If nothing else works, return n, the largest factor solos!
    return n
PRIME_LIST = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]