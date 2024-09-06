```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    counts = 0
    for num in range(1, n+1):
        if (num % 11 == 7) or (num % 13 == 7):
            counts += 1
    return counts

# Test the function
for i in range(50, 78, -1):
    print(fizz_buzz(i), end=' ')
```