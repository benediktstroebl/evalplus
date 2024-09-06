Here is a Python script that defines a function fizz_buzz which calculates the number of times the digit 7 appears in integers less than a given number n that are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(1 for digit in range(10, n + 1) if digit == 7 and n % 11 == 0 or n % 13 == 0)

# Test suite
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```