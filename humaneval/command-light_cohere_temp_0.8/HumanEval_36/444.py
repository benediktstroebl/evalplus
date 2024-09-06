Here is a Python script that contains a self-contained function called `fizz_buzz` that solves the problem you provided:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(2, n+1):
        if int(str(i))[1] == 7 and i % 11 == 0 or i % 13 == 0:
            count += 1
    return count

# Test cases
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```

This script defines a function `fizz_buzz` that takes an integer n as input and returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The function uses a iterative approach to achieve this, it checks if the digit at position 1 of the given number is 7 and whether the number is divisible by 11 or 13, and then increments the count.

The test cases provided are used to validate the function, ensuring that it returns the expected results for the given inputs.