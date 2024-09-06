```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        if (num % 11 == 7) or (num % 13 == 7):
            count += 1
    return count

# Test the function with different input values
assert(fizz_buzz(50) == 0)
assert(fizz_buzz(78) == 2)
assert(fizz_buzz(79) == 3)
assert(fizz_buzz(100) == 5)
assert(fizz_buzz(23) == 0)
assert(fizz_buzz(9) == 0)
```