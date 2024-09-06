```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    c = 0
    for i in range(1, n+1):
        digit = ord('7')
        while any(map(lambda x: x <= i and x >= 0 and x != digit, range(10))) and i % 11 == 0 or i % 13 == 0:
            c += 1
        i += 1
    return c
```