
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    srtd_primes = prime_sieve(100)
    i = 0
    while i < len(srtd_primes):
        if srtd_primes[i] * srtd_primes[i] * srtd_primes[i] <= a:
            i += 1
        else:
            break
    return i == len(srtd_primes)
