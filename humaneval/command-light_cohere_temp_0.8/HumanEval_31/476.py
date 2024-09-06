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

The code defines a function `is_prime` that checks whether a given number `n` is prime or not. It uses a basic logic to iterate through the square root up to the square root of `n` (excluding `n` itself and its multiples of 2 and 3) and checks for divisibility. The function returns `True` if the number is prime and `False` otherwise. 

The function is then tested with various input values and the results are printed, showing the function's ability to correctly identify prime numbers.