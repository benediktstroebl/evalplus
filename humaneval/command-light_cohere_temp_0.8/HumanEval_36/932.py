```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = ord('7')
        if (i % 11 == 0 or i % 13 == 0) and (i + digit - 1 > 0 and i + digit - 1 <= n):
            count += 1
    return count
```