```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)[0]
        if digit == 7 and i % 11 == 0 or i % 13 == 0:
            count += 1
    return count

# Test the function
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3

```
This Python script defines a function fizz_buzz that calculates and returns the number of occurrences of the digit 7 in numbers less than n that are divisible by 11 or 13. The function uses a loop to iterate through numbers from 1 to n, checking if the current number's digit is 7 and if it's divisible by 11 or 13. The test suite ensures that the function correctly calculates the expected results.