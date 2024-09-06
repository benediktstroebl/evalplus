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
The function `is_prime` takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. The function uses a algorithm to check for primality. The function first checks if `n` is less than or equal to 1, in which case it is not prime. It then checks if `n` is less than 3, which is also not prime. The function then checks if `n` is even or odd and whether it can be expressed as 2n or 3n + 1, in which case it is not prime. The function then checks if `n` is a perfect square or a perfect cube, which are also not prime. The function then checks if `n` is a perfect square root, and if it is divisible by any number of the form 5i + 1. Finally, if none of these conditions are met, the function returns `False`, indicating that `n` is not a prime number.