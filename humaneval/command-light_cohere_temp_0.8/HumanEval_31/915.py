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

# Unit tests
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
This code defines a function called `is_prime` that checks whether a given number `n` is a prime number or not. It uses some simple rules and tests to determine primality, such as `n <= 1` which is an edge case, `n <= 3` which is simple, `n% 2 or 3 == 0` which are common divisors, and a while loop that checks for divisibility up to the square root of `i` where `i` starts at 5 and increases by 6 each time `i` is less than `n`.  The test returns `True` if the condition is met, and `False` otherwise.