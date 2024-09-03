def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers and false otherwise."""
    # Check if a is divisible by 2 or 3
    if (a <= 2) or (a % 2 == 0) or (a % 3 == 0):
        return False

    # Check if a is a multiplication of two primes
    for p in range(2, int(a ** 0.5) + 1):
        if a % (p * p) == 0:
            return False

    return True