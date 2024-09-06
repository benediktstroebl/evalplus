
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        return False
    i = 0
    while i < a:
        if is_prime(i):
            i += 1
        else:
            return is_primes_multiply(i)
    return True
