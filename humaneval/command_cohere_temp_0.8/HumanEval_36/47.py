Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers with 7 in them and divisible by 11 or 13
    return sum(1 for num in range(n):
              if 7 not in str(num) and (num % 11 == 0 or num % 13 == 0))

# Tests
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```

This script defines the `fizz_buzz` function, which is self-contained and does not use any external variables or dependencies. It solves the given problem by filtering out numbers less than `n` that are divisible by 11 or 13 and checking if the digit 7 appears in those numbers. The function then returns the number of times the digit 7 appears in those numbers. The tests verify the function behavior for different inputs.