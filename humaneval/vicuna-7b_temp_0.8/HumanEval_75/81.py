
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 10:
        return False
    p1, p2, p3 = primes[a//3], primes[a//3+1], primes[a//3+2]
    if a%p1 == 0 or a%p2 == 0 or a%p3 == 0:
        return False
    n = a
    while True:
        n += 2
        if n % p1 == 0 or n % p2 == 0 or n % p3 == 0:
            return False
        if n > 100:
            break
    return True