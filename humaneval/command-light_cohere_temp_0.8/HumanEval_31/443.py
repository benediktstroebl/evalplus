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

# Test cases
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This function is_prime takes an integer n as input and returns True if n is a prime number, and False otherwise. The function implements the basic primality tests: divisibility by 2 and 3, checking for divisibility by consecutive numbers starting from 5, and finally checking for divisibility by sqrt(n) itself or (n + 2).

This function can be used to determine whether a given number is prime or not, which is useful in many mathematical and coding applications.