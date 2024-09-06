```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    s = sum(1 for digit in str(n) if digit == 7)
    return s if 11 <= n <= 13 else s + 1
```