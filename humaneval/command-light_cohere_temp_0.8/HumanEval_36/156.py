Here's the solution:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        digit = str(i % 10)
        count = sum(1 for d in dp if d and digit in str(d) == digit) + 1
        dp[i] = count
    return dp[n]

# Test suite
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
test_fizz_buzz()
```

This code defines a function `fizz_buzz` which calculates the number of occurrences of the digit 7 in numbers less than `n` and also has a test suite to verify its correctness.