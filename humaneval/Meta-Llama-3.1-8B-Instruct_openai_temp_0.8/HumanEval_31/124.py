```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Corner cases: numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check divisibility up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # If no divisors are found, the number is prime
    return True

# Test cases
print(is_prime(6))    # False
print(is_prime(101))  # True
print(is_prime(11))   # True
print(is_prime(13441)) # True
print(is_prime(61))   # True
print(is_prime(4))    # False
print(is_prime(1))    # False
```

This script defines a function `is_prime(n)` that checks whether a given integer `n` is prime or not. It uses a simple trial division method to check for divisibility up to the square root of `n`. The script also includes the test cases from the original problem as comments.