```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    if n <= 0: return 0
    count = 0
    for i in range(1, n+1):
        num = 0
        while (i % 11 == 0 or i % 13 == 0) and i > 0:
            num += 1
        if num == 7:
            count += 1
    return count
```