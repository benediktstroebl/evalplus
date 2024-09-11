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
    # Handle edge cases: numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check for divisibility from 2 to the square root of n
    # We only need to check up to the square root because a larger factor of n would be a multiple of smaller factor that has already been checked
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by any number between 2 and its square root, it's not prime
        if n % i == 0:
            return False
    
    # If n is not divisible by any number between 2 and its square root, it's prime
    return True

# Test cases
print(is_prime(6))       # False
print(is_prime(101))     # True
print(is_prime(11))      # True
print(is_prime(13441))   # True
print(is_prime(61))      # True
print(is_prime(4))       # False
print(is_prime(1))       # False
```

This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It first handles edge cases where `n` is less than 2, then checks for divisibility from 2 to the square root of `n`. If `n` is not divisible by any of these numbers, it's considered prime. The script also includes test cases to demonstrate the function's correctness.