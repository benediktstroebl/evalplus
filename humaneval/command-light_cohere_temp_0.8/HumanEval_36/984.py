```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(c == 7 for c in str(i) for i in range(10, n+1) if i % 10 == 0 and i % 100 != 0 and i % 400 != 0)

# Test the function
assert fizz_buzz(50) == 0, "Function failed test"
assert fizz_buzz(78) == 2, "Function failed test"
assert fizz_buzz(79) == 3, "Function failed test"
```