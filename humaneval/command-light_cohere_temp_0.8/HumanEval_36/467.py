Here's the function:
```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(x == 7 for x in range(1, n + 1) if x % 10 != 7 and x % 100 != 7)
```
Now you can call this function with different input numbers to get the expected results.