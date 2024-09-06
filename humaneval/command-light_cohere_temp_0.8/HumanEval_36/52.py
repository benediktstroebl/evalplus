```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = int(str(i)[1])
        if (digit % 10 != 7) or (digit > 4 and digit < 13):
            count += 1
    return count
```