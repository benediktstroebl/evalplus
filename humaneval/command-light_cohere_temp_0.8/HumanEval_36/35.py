Here is a self-contained Python script with a function that solves the problem you provided:
```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    sum = 0
    for i in range(1, n+1):
        digit = str(i)[0]
        if digit == 7 and (i % 11 == 0 or i % 13 == 0):
            sum += 1
    return sum
```
This script defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than `n` which are either divisible by 11 or 13. It uses a own classic approach using a loop to iterate through numbers up to `n` and checks for the digit 7 and divisibility by 11 or 13. The function returns the result, which represents the number of times the digit 7 appears in such numbers.