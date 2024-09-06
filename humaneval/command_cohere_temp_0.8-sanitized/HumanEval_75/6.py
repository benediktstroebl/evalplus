def is_multiply_prime(n):
    """
    Checks if n is a product of three primes.
    """
    if not isinstance(n, int) or n < 0 or n > 100:
        return False

    # checking for 2, 3 and 5 as divisors
    for i in [2, 3, 5]:
        if n % i == 0:
            return False

    return all(prime_numbers(n))