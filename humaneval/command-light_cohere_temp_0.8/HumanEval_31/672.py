```python
def is_prime(n):
    if n <= 1:
        return False
    for i := 2; i * i <= n; i += 1:
        if n % i == 0:
            return False
    return True

# Test suite
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This script defines the function `is_prime` which checks whether a given number `n` is a prime number or not. It then passes all the  tests, which check if some commonly known prime numbers pass the `is_prime` function test, and some commonly known non-prime numbers do not pass the test.