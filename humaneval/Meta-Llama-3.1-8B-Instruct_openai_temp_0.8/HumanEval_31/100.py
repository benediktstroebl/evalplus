### Prime Number Checker
#### Python Script

```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    Args:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:  # 0 and 1 are not prime numbers
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # All other even numbers are not prime
        return False
    max_divisor = int(n**0.5) + 1  # Only need to check up to the square root of n
    for d in range(3, max_divisor, 2):  # Check odd numbers only
        if n % d == 0:
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

This script defines the `is_prime` function, which checks if a given number `n` is prime by checking divisibility up to the square root of `n`. It returns `True` if `n` is prime and `False` otherwise. The test cases at the end demonstrate the function's usage and correctness.