def is_multiply_prime(a):
    """
    Returns True if a is the multiplication of 3 prime numbers and False otherwise.
    Checks if a is divisible by 2 and 3, then it is divisible by their product.
    If the product of the pair of primes is a prime
    """
    return a % (2*3) == 0