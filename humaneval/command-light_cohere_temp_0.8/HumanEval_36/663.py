```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        if (num % 11 == 0 or num % 13 == 0) and str(num)[-[7] != '7':
            count += 1
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

The function fizz_buzz takes an integer n as input and returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The function uses a loop and a condition to check if the current number is less than n and the number is divisible by 11 or 13, and if it meets the condition, the count is incremented.