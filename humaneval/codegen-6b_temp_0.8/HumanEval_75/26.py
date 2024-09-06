
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    global primes
    new_primes = primes[:]
    for n in xrange(2,a):
        for m in new_primes:
            if n % m == 0:
                break
            elif m > n**0.5:
                primes.append(n)
                break
    if a % primes[-1] == 0:
        return True
    else:
        return False

