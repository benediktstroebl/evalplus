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
```
This function, named `is_prime`, takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function uses several tests to check for primality:
- If `n` is less than or equal to 1, it is definitely not a prime number.
- If `n` is 2 or 3, it is a prime number.
- If `n` is a multiple of 2 or 3, it is definitely not a prime number.
- The function then checks for divisibility by small numbers up to the square root of `n`, using a simple iterative method.