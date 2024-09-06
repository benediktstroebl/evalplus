```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)
        if (7 in digit) and ((digit[digit.index(7)] % 10) == 0) and ((digit[0] == 11) or (digit == "13")):
            count += 1
    return count
```