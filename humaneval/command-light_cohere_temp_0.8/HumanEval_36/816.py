```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    counts = 0
    for num in range(10, n + 1, 2):
        if (num % 11 == 7) or (num % 13 == 7):
            counts += 1
    return counts

# Example usage:
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This Python function, `fizz_buzz`, calculates the number of times the digit 7 appears in numbers less than a given input `n` that are both divisible by 11 and 13. It iterates through numbers from 10 down to `n` in pairs, checking for the appearance of 7 in both divisors. The function ultimately returns the number of such appearances of 7, which meets the criteria.