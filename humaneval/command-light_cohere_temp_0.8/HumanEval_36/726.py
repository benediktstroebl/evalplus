```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    if n < 0:
        return "Error"
    c = 0
    for i in range(1, n+1):
        if int('7' + str(i)) % 10 == 0 and i % 11 == 0 or i % 13 == 0:
            c += 1
    return c
```