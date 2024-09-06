```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        if (num % 11 == 0 or num % 13 == 0) and (7 in str(num)):
            count += 1
    return count

# Test the function
for i in range(80):
    assert fizz_buzz(i) == 0 if i <= 50
    assert fizz_buzz(i) == 1 if i >= 50 and i % 2 == 0
    assert fizz_buzz(i) == 2 if i >= 53 and i % 3 == 0
    assert fizz_buzz(i) == 3 if i >= 56 and i % 5 == 0
```