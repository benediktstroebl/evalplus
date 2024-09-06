```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    sum = 0
    for i in range(1, n+1):
        digit = str(i % 10)[2]
        if digit == '7':
            sum += 1
        if sum > 10:
            return 10
    return sum
```