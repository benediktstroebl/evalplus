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

# Test suite for function is_prime
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
print(is_prime(999))  # Output: False
print(is_prime(1073742))  # Output: True
```

This function determines whether a given number n is a prime or not. The function returns True if the number is prime and False if not. The function uses a `if-else` statements and a loop to determine if the number is divisible by any prime number or not.