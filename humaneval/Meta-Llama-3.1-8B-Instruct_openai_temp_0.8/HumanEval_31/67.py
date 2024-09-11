```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
    Args:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    
    Examples:
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
    
    # Corner case: numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # Check if the number is divisible by any number up to its square root
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # If the number is not divisible by any number up to its square root, it is prime
    return True


# Test the function
print(is_prime(6))    # False
print(is_prime(101))  # True
print(is_prime(11))   # True
print(is_prime(13441))# True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```

This code defines a function `is_prime` that checks whether a given number `n` is prime. It does this by checking for divisibility by numbers up to the square root of `n`, which is a common optimization technique for primality testing. If `n` is divisible by any of these numbers, it is not prime. Otherwise, it is prime. The function is then tested with the example inputs provided in the docstring.