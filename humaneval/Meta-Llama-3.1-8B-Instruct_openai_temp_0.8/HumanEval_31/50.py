```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Handle edge cases where n is less than or equal to 1
    if n <= 1:
        return False
    
    # Check if n is divisible by any number up to its square root
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    # If n is not divisible by any number up to its square root, it's prime
    return True

# Test the function
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines a function `is_prime(n)` that checks if a given number `n` is prime. It returns `True` if `n` is prime and `False` otherwise. The function uses a simple trial division method to check for primality, which is sufficient for small to medium-sized integers. For larger integers, more advanced primality tests such as the Miller-Rabin primality test may be necessary.