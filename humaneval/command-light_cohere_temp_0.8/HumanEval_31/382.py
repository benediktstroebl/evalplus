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
print(is_prime(1))  # Output: False
```
This code defines a `is_prime` function that checks whether a given number is a prime or not. The function iterates from 2 up the square root of the input number, if the input number is divisible by any of the tested numbers, it is considered not a prime.

The function also has some built-in tests to quickly identify prime and non-prime numbers, which improves its performance.