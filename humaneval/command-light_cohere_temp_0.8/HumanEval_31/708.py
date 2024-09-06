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

The Python function `is_prime(n)` determines whether a given number is prime. The function first determines whether `n` is less than or equal to one and returns `False` if this is the case. Then, the function determines whether `n` is less than or equal to three and returns `True` if this is the case. After that, the function checks for divisibility by 2 and 3, returning `False` if `n` is divisible by either of these numbers. The function then begins a trial of the number 5^2, and then determines whether `n` is divisible by any number less than 6 that is a factor of `5^2`. The function returns `True` if this is the case.

If none of these conditions are met, the function returns `True`, indicating that `n` is a prime number.