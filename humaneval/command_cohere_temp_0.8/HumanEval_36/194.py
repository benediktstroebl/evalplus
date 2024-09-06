Here's a Python script with a self-contained function `fizz_buzz` that solves the problem:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers divisible by 11 or 13 and count sevens
    return sum(7 in str(x) for x in range(1, n+1) if not (x % 11 == 0 or x % 13 == 0))
```
This approach directly filters out numbers less than `n` that are divisible by 11 or 13 and then counts the number of sevens in those numbers using a generator expression.

To test this function, you can run the following code:
```python
# Test the function against known inputs
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```

This demonstrates how the function `fizz_buzz` solves the problem in a self-contained manner.