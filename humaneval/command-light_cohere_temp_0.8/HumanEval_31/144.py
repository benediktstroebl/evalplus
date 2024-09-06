Here's the improved Python script with the self-contained function:
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

The function checks for primality by following these rules:
- If `n` is less than or equal to 1, it returns `False`.
- If `n` is 2 or 3, it returns `True`.
- Then, it checks for divisibility by `2` and `3`, returning `False` if it fails.
- Next, it checks if `n` is a square or cube (up to the fifth power), and returns `False` if so.
- Then starts a square root of `n` (up to the fifth power), and checks if `n` is divisible by any of these square roots, or the sum of two of their square roots.

- If none of these conditions hold, it returns `True`, indicating that `n` is a prime number.