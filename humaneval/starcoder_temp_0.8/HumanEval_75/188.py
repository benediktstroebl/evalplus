
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_list = get_primes_list(100)
    for prime in prime_list:
        if a % prime == 0:
            if a / prime in prime_list:
                return True
    return False

