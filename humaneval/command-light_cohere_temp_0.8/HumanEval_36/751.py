```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    i = n
    while i > 0:
        digit = str(i % 10)
        if digit == '7':
            count += 1
        i //= 13
    return count
```