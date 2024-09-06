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

The function `is_prime` takes a number `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function uses an `if` algorithm to determine whether a given number is prime.

The function first checks if `n` is less than or equal to `1`, and returns `False` since prime numbers must be greater than `1`. The function then checks if `n` is of the form `2` or `3`, and returns `False` since these are not prime numbers. The function then initializes a `i` to `5` and iterates until the square of `i` is less than or equal to `n`. The function then checks if `n` is divisible by `i` or `i + 2`, and returns `False` if this is the case. The function then checks if `n` is divisible by `i + 6`, and returns `False` if this is the case. Finally, the function returns `True` since it has passed all the tests.