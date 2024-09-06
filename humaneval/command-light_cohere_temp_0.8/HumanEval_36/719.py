Here is a self-contained Python script that defines a function `fizz_buzz` that solves the problem you have described:

```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(int(i) == 7 and i % 11 == 0 or i % 13 == 0 for i in range(1, n+1))

# Test suite
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```

This script defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in integers less than `n` which are divisible by 11 or 13. The function uses a logical `AND` statement to check for divisibility, and the `sum` function to count the occurrences. The `test_fizz_buzz` function contains test cases that validate the function's behavior for different input values.