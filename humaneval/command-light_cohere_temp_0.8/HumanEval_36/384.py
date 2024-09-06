```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(c == 7 for c in str(n + 1) if c.isdigit() and string. 10 if n >= 10 else 9 if n < 50 else 8)
```