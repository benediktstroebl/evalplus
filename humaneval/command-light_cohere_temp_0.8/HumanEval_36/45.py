Here's a self-contained Python script with a function that solves the problem of counting occurrences of the digit 7 in numbers less than a given input n, which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(x == 7 for x in range(1, n + 1) if x % 11 == 0 or x % 13 == 0)

# Test the function
# Expected output: 0
fizz_buzz(50)

# Expected output: 2
fizz_buzz(78)

# Expected output: 3
fizz_buzz(79)
```

This function, `fizz_buzz`, takes an integer n as input and returns the number of occurrences of the digit 7 in numbers less than n that are divisible by 11 or 13. 

This function is self-contained, and it does not require any external variables or functions. It uses a specific to do the task of counting occurrences of a digit and can be efficiently implemented and tested in the Python language.