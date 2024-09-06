
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Create a list of primes under 100
    primes = [i for i in range(1, 101) if is_prime(i)]
    
    # Check if any of the primes are equal to a
    for prime in primes:
        if a == prime:
            return False
    
    # If none of the primes are equal to a, it must be a multiple of the primes
    for i in primes:
        if a % i == 0:
            return False
    
    return True