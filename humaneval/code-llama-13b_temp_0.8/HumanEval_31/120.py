

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
    #First, check if it's a even number.
    if n % 2 == 0:
        return False

    #all other even numbers > 2 are not prime
    #Loop through all odd numbers (starting at 3 and incrementing by 2)
    for i in range(3, n, 2):
        #if we find a number that completely divides n, then it's not prime
        if n % i == 0:
            return False

    #otherwise, n is prime
    return True


