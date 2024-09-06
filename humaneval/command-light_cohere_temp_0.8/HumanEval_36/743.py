Here's a self-contained Python function that solves the problem you described:

```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    divisible = [i for i in range(1, n+1) if (7 % i) == 0 and i % 15 == 0]
    return len(divisible)
```

This function uses list comprehension and basic condition checking to solve the problem. The function will return the times the digit 7 appears in integers less than the number n that are divisible by 11 or 13.