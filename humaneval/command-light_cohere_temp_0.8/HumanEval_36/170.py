```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(d==7 for d in range(10, n+1) if (n%11==0 or n%13==0))

# Test suite
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```
The function fizz_buzz uses a generator expression to sum up the counts of digits 7 in numbers less than n and that are divisible by 11 or 13.