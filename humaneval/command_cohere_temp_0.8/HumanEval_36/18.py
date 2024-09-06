Here's a Python script that contains a function fizz_buzz(n) which solves the problem as per the test cases provided:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out the numbers divisible by 11 or 13, then count sevens.
    return sum(7 in str(x) for x in range(1, n+1) if (x % 11 == 0 or x % 13 == 0))
```
This will return the count of 7s in numbers below n that are divisible by 11 or 13.