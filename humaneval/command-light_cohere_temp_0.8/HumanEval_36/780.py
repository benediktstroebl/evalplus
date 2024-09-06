```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = ord('7')
        if i % 10 == digit:
            if (i % 11 == 0) or (i % 13 == 0):
                count += 1
    return count

# Test suite
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
assert fizz_buzz(100) == 5
assert fizz_buzz(121) == 4
assert fizz_buzz(27) == 1
```