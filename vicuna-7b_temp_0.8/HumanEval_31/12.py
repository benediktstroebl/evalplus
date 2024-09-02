

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
    # Use a hash to store the first n/2 prime numbers, 2 <= n < 1000.
    # Check if the candidate number n is divisible by any of the first n/2 prime numbers.
    # If not, return True, otherwise return False.
    
    # Initialize the first n/2 prime numbers, 2 <= n < 1000.
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    # Check if the candidate number n is divisible by any of the first n/2 prime numbers.
    for prime in prime_numbers:
        if n % prime == 0:
            return False
    
    # Return True, since n is not divisible by any of the first n/2 prime numbers.
    return True
