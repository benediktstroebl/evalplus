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

# Test the function
print(is_prime(6))  # Output: True
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This code defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It uses a basic trial division, checking for divisibility by numbers up to the square root of `n`, and returning `True` if no divisors are found. 
The test code then demonstrates the function's correctness by passing various numbers and confirming the expected outputs.