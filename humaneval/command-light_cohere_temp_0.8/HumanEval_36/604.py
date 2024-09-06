```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    cnt = 0
    for i in range(1, n+1):
        digit = ord('7') + (i - 1)
        if all(c for c in str(str(i)) if c == digit):
            continue
        if i % 11 == 0 or i % 13 == 0:
            cnt += 1
    return cnt
```