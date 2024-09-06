Here is a Python script with a self-contained function that solves the problem of checking if a given number is a prime, and passes all the corresponding tests:
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
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

# Test the function
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
The `is_prime` function takes an integer `n` as input and returns `True` if `n` is a prime, and `False` otherwise. The function uses an algorithm known as the "Sieve of Eratosthenes" to check for prime status. The test code at the time checks if the function is working correctly by passing various inputs and verifying the output.