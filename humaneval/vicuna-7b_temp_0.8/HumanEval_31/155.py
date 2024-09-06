

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
    # If the input is 0 or 1, then it is certainly prime.
    if n == 0 or n == 1:
        return True
    
    # If the input is a prime number, then it is certainly prime.
    if n in prime_numbers:
        return True
    
    # Otherwise, we need to check the number to see if it is prime.
    # We do this by checking if it is divisible by any number less than its square root.
    # If it is not, then it is certainly prime.
    # Otherwise, we need to check it more carefully.
    
    # Calculate the square root of the number.
    x = sqrt(n)
    
    # Check if the number is divisible by any number less than its square root.
    if n % x == 0:
        return False
    
    # If the number is not divisible by any number less than its square root, then it is certainly prime.
    return True
