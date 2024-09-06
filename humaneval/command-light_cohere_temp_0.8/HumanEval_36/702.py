```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        num = str(i)
        num = [c for c in num if c == '7'][0]
        if num == 7 and int(num) < 10:
            count += 1
        if num == 10 or num == 11 or num == 13:
            break
    return count
```