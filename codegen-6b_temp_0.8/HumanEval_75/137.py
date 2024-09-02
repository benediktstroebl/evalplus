
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # First calculate the 3 primes until a % 3 == 0
    while a % 3 == 0:
        a //= 3
        if is_prime(a):
            continue
        else:
            return False
    # Now that a is not a multiple of 3, we can calculate 4 * a + 5 until both a & 5 are prime
    while a % 5 == 0:
        a //= 5
        if is_prime(a):
            continue
        else:
            return False
    # Since a is no longer a multiple of 5, we know this is not a prime number
    return False
