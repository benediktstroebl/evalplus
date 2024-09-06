Here's the self-contained Python function that solves the problem:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(2, n+1):
        if (num % 11 == 7) or (num % 13 == 7):
            count += 1
    return count
```

This function iterates through numbers less than `n`, and checks if the number is divisible by both 11 and 13. If it finds the factory, it increments the count of how many times the digit 7 appears in the range. 

The function is then tested using the provided input.