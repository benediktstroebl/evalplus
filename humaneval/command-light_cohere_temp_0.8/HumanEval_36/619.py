```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(c == 7 for c in str(n) if c.isdigit() andisdivisible(11) or c.isdigit() anddivisible(13))

# Test the function
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```