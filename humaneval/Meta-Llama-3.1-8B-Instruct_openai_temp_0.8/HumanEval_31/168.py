Here's a self-contained Python script that implements the `is_prime` function:
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Test cases
print(is_prime(6))  # Expected output: False
print(is_prime(101))  # Expected output: True
print(is_prime(11))  # Expected output: True
print(is_prime(13441))  # Expected output: True
print(is_prime(61))  # Expected output: True
print(is_prime(4))  # Expected output: False
print(is_prime(1))  # Expected output: False
```
This script defines the `is_prime` function, which checks whether a given number `n` is prime by attempting to divide it by numbers up to its square root. If `n` is divisible, it is not prime; otherwise, it is. The test cases at the end demonstrate the function's correctness.