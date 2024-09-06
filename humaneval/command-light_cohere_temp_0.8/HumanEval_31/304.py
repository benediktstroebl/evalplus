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
This Python code defines a function named `is_prime` that checks whether a given number is prime or not. The function utilizes a well-known primality tests, such as divisibility by 2 and 3, and then checks for divisibility by numbers forming the square of the original number, before finally returning `True` if the number is prime and `False` otherwise. This script then demonstrates the general primality test logic and could be applied to determine if a number is prime or not in a wide range of cases.