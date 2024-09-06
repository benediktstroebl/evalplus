```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)[0]
        if digit == 7 and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

# Test the function with various input values
 assert fizz_buzz(50) == 0
 assert fizz_buzz(78) == 2
 assert fizz_buzz(79) == 3
 assert fizz_buzz(30) == 1
 assert fizz_buzz(72) == 3
 assert fizz_buzz(51) == 4
 assert fizz_buzz(13) == 5
```