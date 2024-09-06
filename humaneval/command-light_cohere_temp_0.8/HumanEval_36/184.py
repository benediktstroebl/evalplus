```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(int(x) == 7 and x <= n and x % 11 == 0 or x % 13 == 0 for x in range(1, n+1))

# Test the function
assert(fizz_buzz(50) == 0)
assert(fizz_buzz(78) == 2)
assert(fizz_buzz(79) == 3)
```