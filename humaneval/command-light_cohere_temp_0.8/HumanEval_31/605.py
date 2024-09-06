```python
def is_prime(n):
    if n <= 1:
        return False
    for i := 2; i * i <= n; i += 1:
        if n % i == 0:
            return False
    return True

# Test code
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1)))  # Output: False
```
This code provides a function `is_prime` that returns true if the number is prime, and false otherwise. The function uses a condition and loop to check if the given number is prime or not.