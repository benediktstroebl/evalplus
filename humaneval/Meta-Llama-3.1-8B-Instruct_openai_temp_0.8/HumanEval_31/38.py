```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
    Parameters:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check for divisors up to the square root of n
        if n % i == 0:  # If n is divisible by i, it's not prime
            return False
    return True

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False
```

This script defines the `is_prime` function, which checks if a given number `n` is prime by iterating from 2 up to the square root of `n` and checking if `n` is divisible by any of these numbers. If `n` is divisible, it's not prime, and the function returns `False`. Otherwise, the function returns `True`. The test cases demonstrate the function's behavior with various inputs.