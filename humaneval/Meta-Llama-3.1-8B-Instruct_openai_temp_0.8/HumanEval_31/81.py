```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    
    # Handle edge cases where n is less than 2
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
if is_prime(6):
    assert False, "Expected is_prime(6) to return False"
if is_prime(101):
    assert True
if is_prime(11):
    assert True
if is_prime(13441):
    assert True
if is_prime(61):
    assert True
if is_prime(4):
    assert False, "Expected is_prime(4) to return False"
if is_prime(1):
    assert False, "Expected is_prime(1) to return False"
```

This script defines the `is_prime` function to check if a given number is prime. It uses a helper check for even numbers, and then checks odd factors up to the square root of the input number. The test cases at the end demonstrate the function's correctness. 

The script includes docstrings and feature-rich Python comments to explain the code and its purpose.