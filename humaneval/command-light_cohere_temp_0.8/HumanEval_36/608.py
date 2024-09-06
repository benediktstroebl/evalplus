```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    seen = 0
    for num in range(1, n+1):
        if (10 <= num) and (num % 11 == 0) or (10 <= num) and (num % 13 == 0):
            seen += 1
    return seen
```