
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Use sieve of Eratosthenes to find all prime numbers less than a
    primes = [True]
    for i in range(a-2, a):
        if (i % 2 == 0):
            primes[i//2] = False
        else:
            primes[i] = True
        
    # Check if a is the product of three primes
    for i in range(3, a-2):
        if (a % i) == 0:
            return False
    return True
