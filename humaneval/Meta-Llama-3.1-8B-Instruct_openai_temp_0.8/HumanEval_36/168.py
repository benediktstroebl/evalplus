```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Should print: 0
print(fizz_buzz(78))  # Should print: 2
print(fizz_buzz(79))  # Should print: 3
```

This Python script defines a function `fizz_buzz(n)` that counts the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It uses a simple loop to iterate over all integers less than `n`, and for each one that is divisible by 11 or 13, it increments a counter by the number of times the digit 7 appears in its string representation. Finally, it returns the total count.