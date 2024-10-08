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

# Example usage:
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1)))  # Output: False
```
This Python code defines a function `is_prime` that checks whether a given number is prime or not. The function employs a foundation of prime numbers, which is that 2 and 3 are the only numbers that are divisible by 2 and 3, and all other prime numbers are divisible by 2 and 3.

This is just one way to solve the problem, and you can always try other methods or algorithms to make your code more efficient or more readable.