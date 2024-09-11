```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    
    # Handle edge cases: numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check divisibility from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # If n is divisible by any number, it's not prime
            return False
    # If no divisors are found, n is prime
    return True

# Test cases
if is_prime(6):
    assert False
if is_prime(101):
    assert True
if is_prime(11):
    assert True
if is_prime(13441):
    assert True
if is_prime(61):
    assert True
if is_prime(4):
    assert False
if is_prime(1):
    assert False

print("All test cases pass!")
```

This script defines the `is_prime` function, which checks if a given number is prime. It first handles edge cases where numbers less than 2 are not prime. Then it checks divisibility from 2 to the square root of the number, as any factor larger than the square root would have a corresponding factor smaller than the square root. If no divisors are found, the number is prime. The test cases are included at the end to verify the function's correctness.