
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    if a > 100:
        return False

    primes = [2, 3, 5] # List of prime numbers
    max_factor = int(a ** 0.5) # Square root of a.
    max_factor_found = False
    for prime in primes:
        max_factor_found = False
        for i in range(prime, max_factor + 1, prime):
            if i * prime > max_factor:
                break
            if i * prime == a:
                max_factor_found = True
                break
        if not max_factor_found:
            break
    return max_factor_found
