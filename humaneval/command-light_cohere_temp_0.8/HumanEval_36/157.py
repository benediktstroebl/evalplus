```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        if (num % 11 == 0 or num % 13 == 0) and 7 == num:
            count += 1
    return count

# Test the function
for i in range(80):
    assert fizz_buzz(i) == 0 or i <= 6
```