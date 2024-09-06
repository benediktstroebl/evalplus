

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
    # This function uses the Sieve of Eratosthenes algorithm to efficiently 
    # determine whether a number is prime or composite.
    # http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    
    # Step 1: Create a boolean array of size 2**32
    # The first 2**32 integers will be prime numbers
    is_prime = [True for i in range(2**32)]
    for i in range(2*3*5*7, 2*3*5*7+32):
        # skip 3 and 5, since 6 is the first composite number
        if i % 3 == 1 or i % 5 == 1:
            continue
        is_prime[i] = False
        
    # Step 2: Check if the number is in the array of prime numbers
    if n in is_prime:
        return True
    return False
