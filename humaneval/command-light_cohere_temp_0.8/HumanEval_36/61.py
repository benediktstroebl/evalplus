```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = ord('7') + (i - 1)
        x = int(str(i)[:-len(str(i))][digit])
        if (x % 11 == 0 or x % 13 == 0):
            count += 1
    return count
```