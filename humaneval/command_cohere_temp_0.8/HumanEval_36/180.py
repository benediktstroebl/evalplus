Here's a Python script with a self-contained function `fizz_buzz` that solves the problem:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers divisible by 11 or 13 and count sevens
    return sum(int(d) == 7 for num in range(1, n + 1) for d in str(num) if num % 11 == 0 or num % 13 == 0)
```

This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the number of times the digit **7** appears in integers less than `n` that are divisible by 11 or 13. This function utilizes built-in Python functionalities to solve the problem efficiently.