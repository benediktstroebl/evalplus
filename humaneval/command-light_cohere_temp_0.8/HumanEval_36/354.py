```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(x in str(i) for i in range(1, n+1)) \
           if (n % 10 == 7) or ((n % 13) == 7) else 0
```