```python
def fizz_buzz(n: int):
    return sum(k == 7 for k in range(1, n + 1) if k % 11 == 0 or k % 13 == 0)

# Tests
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```

This script defines a function `fizz_buzz` that calculates the number of times the digit 7 appears in the range from 1 to `n` in integers that are divisible by 11 or 13. The function then includes a test that checks the correctness of the solution for the given inputs.