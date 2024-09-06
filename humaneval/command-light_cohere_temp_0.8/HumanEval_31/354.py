```python
def is_prime(n):
    """Returns True if n is prime, False otherwise."""
    if n < 2:
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

# Test suite
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This code defines a function `is_prime` that checks if a given number `n` is prime or not. It uses some basic primality checks, such as `n` greater than 1 and `n` odd, and more advanced tests like checking divisibility by consecutive odd numbers up to the square root of `n`. The test suite ensures that the function works correctly for a variety of inputs.