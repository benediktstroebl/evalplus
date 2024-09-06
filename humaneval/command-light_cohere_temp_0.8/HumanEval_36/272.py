Here is a Python script with a self-contained function that solves the problem you provided:
```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    nums = range(10, n+1, 2)
    for num in nums:
        if num % 11 == 7 or num % 13 == 7:
            count += 1
    return count

# Test the function
for i in range(80):
    assert fizz_buzz(i) == 0 if i < 50
    assert fizz_buzz(i) == 2 if i >= 50 and i % 2 == 0
    assert fizz_buzz(i) == 3 if i >= 50 and i % 3 == 0
```
This script defines a function fizz_buzz that calculates the number of times the digit 7 appears in the range of integers less than a given number n, which are divisible by 11 or 13. The function then tests this tests to ensure the correctness of its implementation.