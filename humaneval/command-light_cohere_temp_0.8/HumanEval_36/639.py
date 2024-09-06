Here's the provided Python script:

```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)[0]
        if digit == '7':
            count += 1
        if (count == 7) and (i % 11 == 0 or i % 13 == 0):
            break
    return count
```