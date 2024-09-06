Here's a self-contained Python script that defines a function `fizz_buzz` that computes and returns the number of times the digit 7 appears in integers less than a given number `n` that are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    if n < 7:
        return 0
    seen = 0
    for i in range(2, n+1):
        digit = 7
        while True:
            if i % 11 == 0 or i % 13 == 0 and i % 10 != 0:
                break
            if i % 10 == digit:
                seen += 1
            digit += 1
    return seen
```
This code defines a function fizz_buzz that takes an integer n as input and returns the number of times the digit 7 appears in integers less than n and divisible by 11 or 13.