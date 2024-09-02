
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
    primes = []
    i = 2
    while i * i <= a:
        if a % i:
            i += 1
        else:
            a = a / i
            primes.append(i)
    if len(primes) != 3:
        return False
    for prime in primes:
        if not is_prime(prime):
            return False
    return True
