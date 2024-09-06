Here's the code:

```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)[-subscript(0)]
        if digit == '7' and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

# Test the function
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```

This script defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than a given input `n` which are divisible by 11 or 13. The function uses a loop and an if statement to identify such numbers, and returns the count of 7s found. The `test_fizz_buzz` function is used to verify the correctness of the `fizz_buzz` function with the provided test values.