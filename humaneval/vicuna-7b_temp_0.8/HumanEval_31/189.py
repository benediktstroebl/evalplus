

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    # This implementation uses the Sieve of Eratosthenes to quickly 
    # determine if a number is prime.
    
    # The Sieve of Eratosthenes is a simple algorithm that 
    # efficiently generates a list of prime numbers.
    sieve = [True for i in range(10)]
    sieve[0] = sieve[1] = True
    sieve[2] = sieve[3] = True
    sieve[5] = sieve[7] = True
    sieve[11] = sieve[13] = True
    sieve[17] = sieve[19] = True
    sieve[23] = sieve[29] = True
    sieve[31] = sieve[37] = True
    sieve[41] = sieve[47] = True
    
    # Check if n is divisible by any of the numbers in the sieve
    for i in range(6, int(n**0.5) + 1, 2):
        if sieve[i]:
            return False
            
    return True
