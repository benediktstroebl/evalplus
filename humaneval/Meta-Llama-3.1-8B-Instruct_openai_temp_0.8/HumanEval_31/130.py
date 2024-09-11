### Prime Number Checker
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if n is prime, False otherwise.
    """
    # Handle edge cases
    if n <= 1:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
    
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    
    # Check odd factors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    # If no factors were found, n is prime
    return True

# Test cases
print(is_prime(6))     # False
print(is_prime(101))   # True
print(is_prime(11))    # True
print(is_prime(13441)) # True
print(is_prime(61))    # True
print(is_prime(4))     # False
print(is_prime(1))     # False
```
This script defines a function `is_prime(n)` that checks whether a given number `n` is prime. It handles edge cases, checks for divisibility by 2, and checks for odd factors up to the square root of `n`. If no factors are found, `n` is prime. The test cases are included at the end to verify the function's correctness.