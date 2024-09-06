```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    nums = range(10, n + 1, 2)
    for digit in nums:
        if (7 <= digit <= 9) and (digit % 11 == 0 or digit % 13 == 0):
            count += 1
    return count
```