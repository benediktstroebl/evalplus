def is_multiply_prime(a):
    # Check if a is the product of 3 primes
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if a == 1:
        return False
    for prime in prime_numbers:
        if a % prime == 0:
            return False
    return True