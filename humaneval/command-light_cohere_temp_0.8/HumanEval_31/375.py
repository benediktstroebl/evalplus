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
The function `is_prime` takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. It uses a if `n <= 1`, which is not a prime number, it returns `False`. If `n` is less than or equal to three, it is also not prime, so it returns `True`. If `n` is even or `n` is less than 6, it checks for the divisibility by 2 and 3, returning `False` if either of these conditions is met. If the number from 5 to the square root of `n` is less than or equal to `n`, it checks if `n` is divisible by any number between 5 and `n` and plus 2. If `n` is divisible by any of these numbers, it returns `False`. If none of these conditions are met, it returns `True`, indicating that `n` is a prime number.