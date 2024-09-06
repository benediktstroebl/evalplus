```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    while n >= 10:
        if (n % 11 == 7) or (n % 13 == 7):
            count += 1
        n //= 2 
    return count

#Test suite
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
assert fizz_buzz(21) == 0
assert fizz_buzz(61) == 1
```