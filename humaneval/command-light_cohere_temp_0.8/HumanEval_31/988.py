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
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

This function, `is_prime()`, determines whether a given number is prime or not. It uses a specific rules to check for primality, such as excluding numbers less than or equal to 1, 2, or 3, and then checking divisibility up to square numbers (checking up to `i * i`).  The function then returns `True` if the number is prime, and `False` otherwise. 

Please note that this function is self-contained and can be used to solve the problem of checking whether a given number is prime or not, as well as passing tests.