```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        if (7 in str(i)) and ((i % 11 == 0) or (i % 13 == 0)):
            count += 1
    return count

# Unit tests
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```
This script defines a function `fizz_buzz` which takes an integer `n` as an argument and returns the number of times the digit 7 appears in integers less than `n` that are divisible by 11 or 13. The function uses a string manipulation to check if the current number contains the digit 7 and then counts the number of such numbers.