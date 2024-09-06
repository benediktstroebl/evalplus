Here's a Python script with a self-contained function `fizz_buzz` that solves the problem:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers divisible by 11 or 13 and count sevens
    return sum(int(d) == 7 for num in range(1, n + 1) for d in str(num) if num % 11 == 0 or num % 13 == 0)
```

This script assumes no external dependencies or imports. It uses a generator expression to iterate through numbers less than `n` that are divisible by 11 or 13 and counts the occurrences of the digit `7` in each number.

The function returns the total count of occurrences of the digit `7` in numbers less than `n` that are divisible by 11 or 13.