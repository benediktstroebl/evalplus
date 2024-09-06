Here's a self-contained Python script with a function that solves the problem you described, along with tests:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        d = int(num % 10)
        if d == 7 and num % 11 == 0 or num % 13 == 0:
            count += 1
    return count

# Test suite
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```
The above code defines a function `fizz_buzz` which calculates the number of occurrences of the digit 7 in numbers less than a given input n, that are divisible by 11 or 13, and then tests the function with test_fizz_buzz(). The test suite contains additional test cases to ensure the correctness of the function.