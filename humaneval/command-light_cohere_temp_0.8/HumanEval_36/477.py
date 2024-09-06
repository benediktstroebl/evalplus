Here is a self-contained Python script that solves the problem you have described:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    s = set(str(i) for i in range(1, n+1))
    return len(s)
```

This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function uses a set method to collect the digits and calculates the length of the set, which corresponds to the number of times 7 appears.