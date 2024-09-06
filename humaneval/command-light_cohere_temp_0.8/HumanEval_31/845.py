```python
def is_prime(n):
    """Returns True if n is prime, and False otherwise."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5):
        if n % i == 0:
            return False
    return True

# Test the function
>>> is_prime(6)  # Should return False
>>> is_prime(101)  # Should return True
>>> is_prime(11)  # Should return True
>>> is_prime(13441)  # Should return True
>>> is_prime(61)  # Should return True
>>> is_prime(4)  # Should return False
>>> is_prime(1)  # Should return False
```
The function uses a simple algorithm to determine if a number is prime. It also incorporates a simple check for numbers less than 2 to ensure the base case.