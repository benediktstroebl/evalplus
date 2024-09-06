```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    nums = range(10, n + 1, 2)
    for num in nums:
        if (num % 11 == 7) or (num % 13 == 7):
            count += 1
    return count

# Unit tests
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```
This script defines a function `fizz_buzz` that calculates the frequency of the number 7 in numbers divisible by 11 or 13 and less than a given number `n`. It also provides unit tests for the `fizz_buzz` function with expected outputs for the provided inputs.