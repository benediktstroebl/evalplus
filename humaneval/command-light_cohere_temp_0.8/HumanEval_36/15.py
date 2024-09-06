```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = ord('7')
        if i % 10 == digit and i % 11 == 0 or i % 13 == digit and i % 13 == 0:
            count += 1
    return count

# Test suite
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```
This code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13. It then provides test suite with assertions that validate the correctness of the function.