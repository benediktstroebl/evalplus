Here is a Python script that defines a function is_prime that checks if a given number is a prime or not, and passes the tests you have provided:
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
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

This script defines a function `is_prime` that checks whether a given number is prime or not. The function first handles small numbers less than or equal to 2 and 3, then checks divisibility by all numbers from 5 down to the square root of the number. It uses a efficient prime checking by squaring and seeing if the number is divisible by its square, or its square plus two.