```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    nums = range(10, n+1, 2)
    for num in nums:
        if (num % 11 == 7) or (num % 13 == 7):
            count += 1
    return count

# Test the function
for i in range(80):
    assert fizz_buzz(i) == 0 or i == 7
```