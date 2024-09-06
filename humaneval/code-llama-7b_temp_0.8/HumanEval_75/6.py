
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = [2, 3, 5]
    a_prime_factor = []
    i = 0
    while i < len(primes):
        if a % primes[i] == 0:
            a_prime_factor.append(primes[i])
        i += 1

    if len(a_prime_factor) > 2:
        return True
    else:
        return False
