Here's a self-contained Python script that defines a function `fizz_buzz` solving the problem you described:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(int(i) == 7 and i <= n and i % 11 or i % 13 for i in range(1, n + 1))

# Test the function
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```
This script defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than n that are divisible by 11 or 13. The function uses the testing via the `assert` assertion to ensure its correctness for the given inputs.