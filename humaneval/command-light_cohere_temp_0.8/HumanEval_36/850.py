```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    counts = 0
    for i in range(1, n+1):
        num = 10**i
        if num % 11 == 0 or num % 13 == 0:
            counts += 1
    return counts
```