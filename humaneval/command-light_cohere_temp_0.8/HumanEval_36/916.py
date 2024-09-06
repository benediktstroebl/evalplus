```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        num = int('0' + str(i))
        if (num % 11 == 0 or num % 13 == 0):
            count += 1
    return count

# Unit tests
assert(fizz_buzz(50) == 0)
assert(fizz_buzz(78) == 2)
assert(fizz_buzz(79) == 3)
assert(fizz_buzz(120) == 4)
assert(fizz_buzz(123) == 5)
assert(fizz_buzz(248) == 6)
assert(fizz_buzz(<?> ) == 0)
```