Here is a Python script with a self-contained function that solves the problem you have described:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    sum = 0
    for i in range(1, n+1):
        digit = str(i)
        count = sum
        for j in range(0, len(digit) - 4):
            if digit[j] == '7':
                count += 1
        if (i % 11 == 0 or i % 13 == 0) and count > 0:
            sum += count
    return sum
```
This script defines a function fizz_buzz that takes an integer n as input and returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.