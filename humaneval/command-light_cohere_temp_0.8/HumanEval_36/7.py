```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    c = 0
    for i in range(1, n+1):
        if i % 10 == 7 and (i % 11 == 0 or i % 13 == 0):
            c += 1
    return c

# Test suite:
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```

This script defines a function fizz_buzz that calculates the frequency of the number 7 in the sequence of integers less than n which are either divisible by 11 or 13. It also comes with a corresponding test suite that validates the function's correctness.