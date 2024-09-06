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
print(is_prime(6))  # Output: False
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
The function `is_prime(n)` takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. The function uses several criteria to determine if a number is prime, such as `n <= 1` (zero is not prime), `n <= 3` (prime numbers are 2 and 3), `n` is of the form `6k + d` where `d` is a divisor of `n`, `n` is odd and `n` is not divisible by 2 or 3, and checks for divisibility up to `sqrt i` for numbers `i` from 5 to the square root of `n`.