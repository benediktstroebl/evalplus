```python
def fizz_buzz(n: int) -> int: 
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    while n > 0:
        n, d = divmod(n, 10)
        count += d == 7
    return count
```