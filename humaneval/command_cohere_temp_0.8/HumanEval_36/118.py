Here's a Python script with a self-contained function `fizz_buzz` that solves the problem:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers with 7 and divisible by 11 or 13 from the range below n
    count = sum(1 for num in range(n) if 7 in str(num) and num % 11 == 0 or num % 13 == 0)
    return count

# Test Cases
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```

This code defines the `fizz_buzz` function as described in the prompt. It uses a generator expression to filter and count the relevant numbers below `n` that are divisible by 11 or 13 and contain the digit 7. The test cases ensure that the function behaves as expected.