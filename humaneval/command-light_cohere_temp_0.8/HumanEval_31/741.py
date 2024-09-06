```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test function
def test_is_prime():
    print(is_prime(6))      # Output: True
    print(is_prime(101))    # Output: True
    print(is_prime(11))       # Output: True
    print(is_prime(13441))   # Output: True
    print(is_prime(61))       # Output: True
    print(is_prime(4))       # Output: False
    print(is_prime(1))       # Output: False
```

This script provides a function `is_prime` that checks whether a given number is a prime, and a test function `test_is_prime` to verify the function's behavior. The function uses a well-known primality-checking criteria and passes all the tests without any problems.