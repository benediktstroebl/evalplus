```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    # Corner cases: numbers less than 2 are not prime
    if n < 2:
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
    
    # If no factors are found, the number is prime
    return True

# Test cases
print(is_prime(6))   # False
print(is_prime(101)) # True
print(is_prime(11))  # True
print(is_prime(13441)) # True
print(is_prime(61))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
```

This script defines a function `is_prime(n)` that takes an integer `n` as input and returns `True` if it's prime and `False` otherwise. The function uses a combination of corner cases and a loop to check for factors up to the square root of `n`. The test cases are executed at the end of the script to demonstrate the function's correctness.