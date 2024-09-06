```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)
        if digit == '7':
            count += 1
        while count == 1 and digit[0] == '7':
            digit = str(int(digit) + 1)
        if (int(digit) <= 11) or (int(digit) <= 13):
            count = 0
    return count
```