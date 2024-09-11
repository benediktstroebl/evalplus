### Prime Number Checker
#### Python Script
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    
    # Edge cases: numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check divisibility from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # If no divisors found, the number is prime
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
This script defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It uses a simple trial division method to check for divisors, which is sufficient for small to medium-sized numbers. The function returns `True` if `n` is prime and `False` otherwise. The test cases at the end demonstrate the function's usage and expected output.