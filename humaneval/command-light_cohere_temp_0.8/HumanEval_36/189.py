Here's a solution:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(x == 7 for x in str(n) if x % 10 == 0 and n - x >= 0)
```