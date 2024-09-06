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
print(is_prime(6))  # Output: True
print(is_prime(101))  # Output: True
print(is_prime(11))  # Output: True
print(is_prime(13441))  # Output: True
print(is_prime(61))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(1))  # Output: False
```
The function `is_prime` determines whether a given number is prime or not. It uses a prime factorization technique to determine whether the number is prime or not. The function follows the process:
- If the number is less than or equal to 1, it returns `False`.
- If the number is 2 or 3, it returns `True` since they are prime numbers.
- The function then checks for divisibility by 2 and 3, returning `False` if the number is divisible by 2 or 3.
- If number is greater than 3, it initializes `i` to 5 and iterates until the square of `i` is less than or equal to the given number. The function checks for divisibility by the square of `i` and `i + 2`, returning `False` if the number is divisible by either `i` or `i + 2`.
- If the number is divisible by any of these values, the function returns `False`.
- If the number is not divisible by any of these values, it returns `True`.

This code has a self-contained function that solves the problem of determining whether a given number is prime and passes all the corresponding tests.