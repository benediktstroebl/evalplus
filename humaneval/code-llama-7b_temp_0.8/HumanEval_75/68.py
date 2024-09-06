
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # 1 - Validate that (a) is less then 100
    if a > 99:
        return False

    # 2 - Count the number of prime factors of a (using Sieve)
    # Create a list of booleans to mark the current primes as "True"
    primes = [True for _ in range(a)]

    # The first prime is 2
    primes[0] = primes[1] = False

    # Start from 2 to a - 1
    for i in range(2, a):
        # Check if i is a prime
        if primes[i] == True:
            # Mark all i * j as "False" (not primes)
            for j in range(2 * i, a, i):
                primes[j] = False
    
    # Count how many are primes
    num_of_primes = 0
    for k in range(a):
        if primes[k] == True:
            num_of_primes += 1

    # 3 - Return True or False
    if num_of_primes == 3:
        return True

    return False

