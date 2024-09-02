
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # since we know it's less than 100, we'll start with a list of primes and check to see if we've
    # found our number. If not, we'll add it, then check.
    primes = [2, 3, 5]

    # if we know the number is divisible by the prime, then we know it's not a multiply prime.
    for prime in primes:
        is_divisible = False
        if a % prime == 0:
            is_divisible = True
        if is_divisible:
            return False
    return True

