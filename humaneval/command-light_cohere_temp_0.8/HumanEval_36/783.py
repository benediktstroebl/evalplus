Here's the self-contained Python script that defines a function `fizz_buzz` solving the problem:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        if (num % 11 == 7) or (num % 13 == 7):
            count += 1
    return count
```

This function uses a loop to iterate through numbers less than or equal to `n`. The function counts the number of times the digit 7 appears in these numbers, which are either divisible by 11 or 13. It returns the particular count value.