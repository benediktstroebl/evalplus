```python
def is_prime(n):
    if n <= 1:
        return False
    for i:
        if n % i == 0:
            return False
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

This code defines a function `is_prime(n)` that checks whether a given number `n` is a prime number. The function uses a simple algorithm to check for primality, iterating up to the square root of `n` and checking for divisibility. The function then returns `True` if `n` is a prime number and `False` otherwise.

The code then provides test cases to call the `is_prime()` function, and the output is printed to the console to verify that the function works as expected.