
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = get_primes(100)
    i = 0
    while i < len(primes) - 2:
        for j in range(i+1, len(primes) - 1):
            for k in range(j+1, len(primes)):
                if a == primes[i] * primes[j] * primes[k]:
                    return True
        i += 1
    return False
