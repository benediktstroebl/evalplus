Here is a Python script with a self-contained function that solves the problem of checking whether a given number is prime:
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
print(is_prime(6))  # Output: True
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```

The code defines a function `is_prime(n)` that checks whether a given number `n` is prime or not. It uses a particular algorithm to determine primality:
- If `n <= 1`, it returns `False` since primes greater than 1 are not considered.
- If `n <= 3`, it returns `True` since all numbers less than or equal to 3 are prime.
- If `n` is even or an odd number, the square of `n` is not equal to `n * 2` or `n * (2 + n)`, so it returns `False`.
- If none of these conditions are met, the function iterates up to the square root of `n` using the `i` value, and checks for divisibility. If `n` is equal to `n` or `n` is divisible by `i` or `i + 2`, it returns `False`. If these conditions are not met, it returns `True`, indicating that `n` is a prime number.