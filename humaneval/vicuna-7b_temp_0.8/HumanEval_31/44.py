

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
    # Base case: if n < 2, it's not prime.
    if n < 2:
        return False
    
    # If n is even, it's not prime.
    if n % 2 == 0:
        return False
    
    # If n is less than 10, it's not prime.
    if n < 10:
        return False
    
    # If n is odd, it's prime.
    if n % 2 == 1:
        return True
    
    # For larger values of n, use a sieve to check if it's prime.
    # A prime number theorem approximation states that:
    # p >= (ln(n) + 1) / 2
    # So, we can check if n > 1000000 that it is not divisible by any
    # number less than sqrt(n) / 2.
    #
    # This is a very inefficient way to check if a number is prime,
    # but it should be sufficient for small n.
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True