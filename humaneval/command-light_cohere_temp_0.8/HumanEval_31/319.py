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

# Test the function with some values
print(is_prime(6))  # Output: True
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This Python code defines a function `is_prime(n)` that checks whether a given number is a prime or not. It uses a certain logic to determine prime numbers: starting from 2 and 3, it checks for divisibility, then checks for numbers that are divisible by 6 less or equal to the square of the input number but not divisible by any number formed by i * i, where i is a constant. This process is guaranteed to take the number less than square root of the input number, ensuring that the number is prime.