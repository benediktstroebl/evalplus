```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    c = 0
    while n >= 10:
        n = n // 13
    if n == 7:
        c += 1
    return c
```